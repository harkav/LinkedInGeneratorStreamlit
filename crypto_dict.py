import yfinance as yf

def create_crypto_dict():
    cryptos = [
    "BTC-USD", "ETH-USD", "USDT-USD", "XRP-USD", "BNB-USD", "SOL-USD",
    "USDC-USD", "TRX-USD", "DOGE-USD", "ADA-USD", "BCH-USD", "LINK-USD",
    "XLM-USD"
]

    data = yf.download(cryptos, period="1d", interval="1m", group_by='ticker')
    latest_prices = {}

    for crypto in cryptos:
        try:
            close_price = data[crypto]["Close"].dropna().iloc[-1]
            latest_prices[crypto] = close_price
            latest_prices = {crypto:  round(price, 2) for crypto, price in latest_prices.items()}
        except (KeyError, IndexError):
            latest_prices[crypto] = None

    return latest_prices

#create_crypto_dict()
