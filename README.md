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
endpoints are partially broken - getting 500 errors across all endpoints aside from health check to root.
- `/stock/{ticker}/price`
- `/stock/{ticker}/historical`
- `/stock/{ticker}/options`
- `/stock/{ticker}/info`
- `/stock/{ticker}/dividends`
- `/stock/{ticker}/earnings`

main issue seems to be yfinance data not playing nice with json (numpy/pandas types being difficult). gotta fix the type conversion before sending responses back.

**need to check expected output for each endpoint:**
1. health check should return basic status + timestamp
2. price endpoint needs clean float values
3. historical data should format dates properly
4. options chain needs readable strike prices
5. company info should strip out any weird data types
6. dividends gotta convert to standard format
7. earnings need proper number formatting


- [ ] metrics to export
  - [ ] stock price fetch latency
  - [ ] successful vs failed yfinance calls
  - [ ] number of unique symbols requested
  - [ ] cache hit/miss ratio (if we add caching)
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

## stuff you need to run this

- python 3.9 or newer
- docker desktop if you want to run containers
- that's pretty much it for now!

## License

MIT License - do whatever you want with this!


