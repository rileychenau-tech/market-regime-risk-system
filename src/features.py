import pandas as pd


def create_features(prices: pd.Series) -> pd.DataFrame:
    """
    Create market regime features from a daily price series.

    Features include:
    - daily return
    - 20-day rolling volatility
    - drawdown
    - 20-day momentum
    - moving average gap
    """

    data = pd.DataFrame()
    data["price"] = prices

    # Daily percentage return
    data["return"] = prices.pct_change()

    # 20-day rolling volatility
    data["volatility_20d"] = data["return"].rolling(window=20).std()

    # Drawdown: how far price is below its historical peak
    running_max = prices.cummax()
    data["drawdown"] = prices / running_max - 1

    # 20-day momentum: return over the past 20 trading days
    data["momentum_20d"] = prices / prices.shift(20) - 1

    # Moving average gap: price compared with 50-day moving average
    moving_average_50d = prices.rolling(window=50).mean()
    data["ma_gap_50d"] = prices / moving_average_50d - 1

    data = data.dropna()

    return data