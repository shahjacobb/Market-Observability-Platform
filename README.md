# Market Data API Observability Platform

An observability platform that tracks real-time performance metrics of YFinance API requests. Built with OpenTelemetry for monitoring, Prometheus for data collection, and Grafana for the UI visualization layer. Everything runs in Docker containers!

## Features
- Get real-time stock data with YFinance
- Monitor system performance using OpenTelemetry
- Collect metrics with Prometheus
- Visualize data through Grafana's UI layer
- Easy deployment with Docker
- FastAPI backend with built-in API docs

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/market-observability-platform.git
   cd market-observability-platform
   ```

2. Start everything up:
   ```bash
   docker-compose up -d
   ```

3. Check out the interfaces:
   - Grafana: [http://localhost:3000](http://localhost:3000)
   - Prometheus: [http://localhost:9090](http://localhost:9090)
   - API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## How It Works

- **Data Collection**: FastAPI grabs the data and tracks metrics
- **Metrics Storage**: Prometheus stores all the data
- **Tracing**: OpenTelemetry helps track system behavior
- **Visualization**: Grafana provides the UI layer for data visualization

## Development

1. Set up your environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   cd backend
   pip install -r requirements.txt
   ```

2. Run the service:
   ```bash
   python -m src.main
   ```

## Deployment

1. Set up your environment variables:
   ```bash
   cp .env.example .env
   # Add your settings to .env
   ```

2. Deploy the containers:
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

## What You Need

- Docker Engine (20.10.0+)
- Docker Compose (2.0.0+)
- Python 3.9+ (for local development)

## License

MIT License - see [LICENSE](LICENSE) for details


