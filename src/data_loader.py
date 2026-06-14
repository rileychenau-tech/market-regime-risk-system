import yfinance as yf


def fetch_prices(
    ticker: str = "NDQ.AX",
    start: str = "2020-01-01",
    end: str | None = None
) -> pd.Series:
    """
    Download daily adjusted close prices from Yahoo Finance.

    Parameters
    ----------
    ticker : str
        Ticker symbol, for example "SPY", "AAPL", or "NDQ.AX".
    start : str
        Start date in YYYY-MM-DD format.
    end : str | None
        End date in YYYY-MM-DD format. If None, downloads up to latest available data.

    Returns
    -------
    pd.Series
        Clean daily price series.
    """
    data = yf.download(
        ticker,
        start=start,
        end=end,
        auto_adjust=True,
        progress=False
    )

    if data.empty:
        raise ValueError(f"No data found for ticker: {ticker}")
    
    # Use closing prices because they give one stable price per trading day,
    # which makes daily return and volatility calculations cleaner.
    prices = data["Close"].dropna()
    prices.name = ticker

    print(f"[data] loaded {len(prices)} daily prices for {ticker}")

    return prices