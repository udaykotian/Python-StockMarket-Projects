import yfinance as yf

# Define the stock symbol (NSE stock with .NS suffix)
stock_symbol = "TCS.NS"

# Fetch the stock data for today
stock = yf.Ticker(stock_symbol)
data = stock.history(period="1d")

# Extract open and close prices
open_price = data['Open'].iloc[0]
close_price = data['Close'].iloc[0]

# Calculate percentage change
percentage_change = ((close_price - open_price) / open_price) * 100

# Prepare the data to save
result = (
    f"Stock: {stock_symbol}\n"
    f"Open Price: {open_price}\n"
    f"Close Price: {close_price}\n"
    f"Percentage Change: {percentage_change:.2f}%\n"
)

# Save to a file
with open("stock_data.txt", "w") as file:
    file.write(result)

# Print the results (for confirmation)
print(result)