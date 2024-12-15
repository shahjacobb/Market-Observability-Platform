from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import time
from functools import wraps

# Request metrics
REQUEST_COUNT = Counter(
    'market_data_requests_total',
    'Total number of requests by endpoint',
    ['endpoint']
)

REQUEST_LATENCY = Histogram(
    'market_data_request_latency_seconds',
    'Request latency in seconds',
    ['endpoint']
)

# YFinance API metrics
YFINANCE_CALLS = Histogram(
    'yfinance_api_duration_seconds',
    'YFinance API call duration in seconds',
    ['operation']
)

# Symbol metrics
SYMBOL_REQUESTS = Counter(
    'stock_symbol_requests_total',
    'Number of requests by stock symbol',
    ['symbol']
)

# Error metrics
ERROR_COUNT = Counter(
    'market_data_errors_total',
    'Total number of errors by type',
    ['error_type']
)

class PrometheusMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        # Track request
        endpoint = request.url.path
        REQUEST_COUNT.labels(endpoint=endpoint).inc()
        
        try:
            response = await call_next(request)
            # Track latency
            duration = time.time() - start_time
            REQUEST_LATENCY.labels(endpoint=endpoint).observe(duration)
            return response
        except Exception as e:
            # Track errors
            ERROR_COUNT.labels(error_type=type(e).__name__).inc()
            raise

def track_symbol_request(symbol: str):
    """Track when a symbol is requested"""
    SYMBOL_REQUESTS.labels(symbol=symbol).inc()

def track_yfinance_operation(operation_name: str):
    """Decorator to track YFinance API call duration"""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            with YFINANCE_CALLS.labels(operation=operation_name).time():
                return await func(*args, **kwargs)
        return wrapper
    return decorator

async def metrics_endpoint():
    """Endpoint for Prometheus to scrape metrics"""
    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    ) 