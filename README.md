# Market Data API Observability Platform

An observability platform ㅁthat analyzes real-time performance metrics and traces of YFinance API requests. Built with OpenTelemetry for monitoring, Prometheus for data collection, and Grafana for the UI visualization layer - uses [Docker-compose](https://docs.docker.com/compose/) to run each service in a Docker container.

## Features
- Get real-time stock data with YFinance
- Monitor system performance using OpenTelemetry through traces
- Collect metrics with Prometheus
- Visualize data through Grafana's UI layer
- FastAPI backend with built-in API docs

## todo
- [x] yfinance api expansion
  - [x] add historical data endpoints (/stock/{ticker}/historical)
  - [x] add company info/profile data (/stock/{ticker}/info)
  - [x] add dividend data (/stock/{ticker}/dividends)
  - [x] add options chain data (/stock/{ticker}/options)
  - [x] add multiple symbol support (/stocks/batch)

  ## Current Status

  ### API Server Setup
  To test the endpoints:
  1. `cd backend/`
  2. Start the server: `uvicorn src.main:app --reload`
  3. The API will be available at `http://localhost:8000`

  ### Endpoint Status

  #### ✅ Working Endpoints
  if you're trying to test these endpoints with curl, download jq to pretty print the JSON responses:
  ```bash
  brew install jq  # on macOS
  ```

  note: all endpoints are case sensitive - use uppercase tickers (AAPL not aapl)

  1. **Health Check**
  ```bash
  curl http://localhost:8000/ | jq '.'
  ```

  2. **Stock Price**
  ```bash
  curl http://localhost:8000/stock/AAPL/price | jq '.'
  ```

  3. **Historical Data**
  ```bash
  # Default 1-month data
  curl http://localhost:8000/stock/AAPL/historical | jq '.'

  # Custom period and interval
  curl "http://localhost:8000/stock/AAPL/historical?interval=1wk&period=1y" | jq '.'
  ```

  4. **Company Info**
  ```bash
  curl http://localhost:8000/stock/AAPL/info | jq '.'
  ```

  5. **Dividends**
  ```bash
  curl http://localhost:8000/stock/AAPL/dividends | jq '.'
  ```

  #### Non-Working Endpoints
  okay these are not working and i need to fix them.
  - Earnings Data (`/stock/{ticker}/earnings`) - Returns NoneType error
  - Batch Stock Data (`/stocks/batch`) - Invalid JSON response
  - Options Chain (`/stock/{ticker}/options`) - Not implemented yet

  ### Development Notes
  - Main focus is on fixing JSON serialization for complex data types (numpy/pandas)
  - Need to implement proper type conversion for:
    - Date formatting in historical data
    - Strike prices in options chain
    - Dividend history formatting
    - Earnings data number formatting

  ### Metrics Implementation
  Added Prometheus metrics to track API performance:
  - Request counts by endpoint
  - Request latency measurements
  - Stock symbol request frequency
  - Error tracking by type
  
  Access metrics at `/metrics` endpoint for Prometheus scraping.

- [ ] metrics to export
  - [x] stock price fetch latency
  - [x] successful vs failed yfinance calls
  - [x] number of unique symbols requested

- [ ] traces to implement
  - [ ] full request lifecycle for each endpoint
  - [ ] yfinance api call duration
  - [ ] data processing time
  - [ ] symbol validation steps
- [ ] docker stuff
  - [ ] create dockerfile for fastapi service
  - [ ] set up docker-compose for local dev
  - [ ] production docker config
- [ ] prometheus setup
  - [ ] collect basic metrics (req/s, latency)
  - [ ] add yfinance-specific metrics
- [ ] grafana dashboards
  - [ ] stock data request performance
  - [ ] yfinance api usage patterns
  - [ ] endpoint usage heatmap
- [ ] opentelemetry implementation
  - [ ] add spans for api endpoints
  - [ ] configure exporters

## How It Works

- **Data Collection**: FastAPI grabs the data and tracks metrics
- **Metrics Storage**: Prometheus stores all the data
- **Tracing**: OpenTelemetry helps track system behavior
- **Visualization**: Grafana provides the UI layer for data visualization

## Testing Prometheus Metrics Output

First, testing some requests to our FastAPI server:
```bash
curl http://localhost:8000/stock/AAPL/price | jq '.' && echo -e "\n" && curl http://localhost:8000/stock/MSFT/price | jq '.' && echo -e "\n" && curl http://localhost:8000/stock/GOOGL/historical | jq '.'
```

Response from endpoints:
![Endpoint Responses](screenshots/endpoint_responses.png)
Shows the price data for AAPL and MSFT, and historical data for GOOGL with customizable time intervals.

Here's the metrics these requests generated:

### Endpoint Hit Counter
```bash
curl http://localhost:8000/metrics | grep market_data_requests_total
```
![Endpoint Hit Counter](screenshots/endpoint_hits.png)
Shows how many times each endpoint was called since the server started. In this case, we see two price endpoint hits (AAPL, MSFT) and one historical data request (GOOGL).

## stuff you need to run this

- python 3.9 or newer
- docker desktop if you want to run containers
- that's pretty much it for now!

## License

MIT License - do whatever you want with this!


