# Market Observability Platform

An observability platform for tracking real-time performance metrics of YFinance API requests. Built to monitor, trace, and analyze system behavior using OpenTelemetry, Prometheus, and Grafana. Containerized with Docker.

## Features
- Real-time stock market data streaming using YFinance
- OpenTelemetry for system monitoring and performance analysis
- Prometheus time-series metrics and data aggregation
- Grafana for UI layer
- Containerized deployment with Docker and Docker Compose
- FastAPI backend with automatic API documentation

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/containerized-market-observability-platform.git
   cd containerized-market-observability-platform
   ```

2. Start the stack:
   ```bash
   docker-compose up -d
   ```

3. Access monitoring interfaces:
   - Grafana: http://localhost:3000
   - Prometheus: http://localhost:9090
   - API Docs: http://localhost:8000/docs

## Architecture

- **Data Collection**: FastAPI service with metric instrumentation
- **Metrics Storage**: Prometheus time-series database
- **Visualization**: Grafana dashboards
- **Tracing**: OpenTelemetry collector and instrumentation

## Development

1. Install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Run service:
   ```bash
   python -m src.main
   ```

## Deployment

1. Set environment variables:
   ```bash
   cp .env.example .env
   # Configure environment variables
   ```

2. Deploy containers:
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

## License

MIT License - see [LICENSE](LICENSE) for details
## Requirements

- Docker Engine (20.10.0+)
- Docker Compose (2.0.0+)
- Python 3.9+ (for local development)

