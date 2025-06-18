import yfinance as yf
import random 

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
def crypto_ticker(prices):
    # Prepare ticker text: e.g. "BTC-USD: 29500.23 | ETH-USD: 1875.45 | ..."
    ticker_text = " | ".join(f"{k}: ${v}" if v is not None else f"{k}: N/A" for k, v in prices.items())

    # Scrolling marquee using CSS animation (works better than deprecated <marquee>)
    ticker_html = f"""
    <div style="overflow:hidden; white-space: nowrap;">
      <div style="
          display: inline-block;
          padding-left: 100%;
          animation: ticker 20s linear infinite;
          font-family: monospace;
          font-weight: bold;
          font-size: 18px;
          color: #ff4500;">
        {ticker_text}
      </div>
    </div>
    <style>
    @keyframes ticker {{
      0% {{ transform: translateX(0%); }}
      100% {{ transform: translateX(-100%); }}
    }}
    </style>
    """
    return ticker_html


def random_top_g_energy(): 
    top_gs = [
    "Sleep is the cousin of bankruptcy. Real kings nap with their eyes open.",
    "If you're not making money while flexing in the mirror, you're already broke.",
    "Every time you hesitate, someone dumber just bought your dream car.",
    "They said money can't buy happiness — so I bought silence.",
    "Wake up. Grind. Flex. Repeat. That's how empires are born.",
    "A Bugatti isn't a car. It's a statement. So is your bank balance.",
    "While you were crying over your ex, I was making six figures by accident.", 
    "Your excuses don't deposit into my account. Try harder.",
    "The only thing standing between you and greatness is your 9-5.",
    "Don't chase women. Chase assets. Women chase assets.",
    "I don't meditate. I dominate.",
    "Billionaire mindset: If you're not wearing sunglasses indoors, you're not thinking big enough.",
    "They laughed when I said I'd make it. Now their daughters are DMing me.",
    "Discomfort builds character. I built mine in a gold-plated gym.",
    "If your haters aren't crying, you're not winning hard enough.",
    "Be the wolf. Eat the sheep. Buy the land.",
    "Your diet, your debt, your DMs — all reflect your discipline.",
    "Crypto isn't dead. It's just waiting for you to stop being a coward.",
    "Success doesn't knock. It revs outside in a matte-black Lambo.",
    "They call it arrogance. I call it receipts."
        
        
    ]
    return random.choice(top_gs)
