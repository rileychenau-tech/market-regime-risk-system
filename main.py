from src.data_loader import fetch_prices


def main():
    ticker = "NDQ.AX"
    start_date = "2020-01-01"

    prices = fetch_prices(ticker=ticker, start=start_date)

    print("\nFirst 5 prices:")
    print(prices.head())

    print("\nLast 5 prices:")
    print(prices.tail())


if __name__ == "__main__":
    main()