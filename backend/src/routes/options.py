from fastapi import APIRouter, HTTPException, Query
from typing import Optional
import yfinance as yf
from datetime import datetime

router = APIRouter(prefix="/stock", tags=["options"])

@router.get("/{ticker}/options")
async def get_options_chain(
    ticker: str,
    date: Optional[str] = Query(None, description="Expiration date (YYYY-MM-DD). If none, returns all available dates")
):
    """Get options chain data"""
    try:
        stock = yf.Ticker(ticker)
        
        # Get all expiration dates if no date provided
        if date is None:
            dates = stock.options
            if not dates:
                return {"ticker": ticker, "options_dates": []}
            return {
                "ticker": ticker,
                "options_dates": [str(d) for d in dates]
            }
            
        # Get specific date options chain
        opt = stock.option_chain(date)
        if opt.calls.empty and opt.puts.empty:
            raise HTTPException(status_code=404, detail=f"No options data found for {ticker} on {date}")
            
        return {
            "ticker": ticker,
            "expiration": date,
            "calls": opt.calls.to_dict(orient='records'),
            "puts": opt.puts.to_dict(orient='records')
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
