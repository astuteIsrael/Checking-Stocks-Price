import yfinance as yf

STK =input("Enter share name: ")

data = yf.Ticker(STK).history(period="1d")

last_market_price = data['close'].iloc[-1]

print("Last market price:", last_market_price)

