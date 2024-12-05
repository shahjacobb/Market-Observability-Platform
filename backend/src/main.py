from fastapi import FastAPI, HTTPException, Query
from typing import Optional
import yfinance as yf
from datetime import datetime

app = FastAPI(title="Stock Market API")

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "online", "timestamp": datetime.now().isoformat()}

@app.get("/stock/{ticker}/price")
async def get_current_price(ticker: str):
    """Get current stock price"""
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period='1d')
        if not data.empty:
            return {
                "ticker": ticker,
                "current_price": data['Close'].iloc[-1],
                "volume": data['Volume'].iloc[-1],
                "timestamp": datetime.now().isoformat()
            }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/stock/{ticker}/historical")
async def get_historical_data(
    ticker: str,
    interval: str = Query(default='1d'),
    period: str = Query(default='1mo')
):
    """Get historical stock data"""
    try:
        stock = yf.Ticker(ticker)
        history = stock.history(period=period, interval=interval)
        
        if history.empty:
            raise HTTPException(
                status_code=404, 
                detail=f"No data found for ticker {ticker}"
            )
            
        return {
            "ticker": ticker,
            "interval": interval,
            "period": period,
            "data_points": len(history),
            "history": history.to_dict(orient='index')
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
