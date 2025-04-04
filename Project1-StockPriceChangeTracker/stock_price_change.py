import yfinance as yf
import os
from datetime import datetime

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

# Get the current date and time
fetch_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Prepare the data to save
result = (
    f"Stock: {stock_symbol}\n"
    f"Fetched on: {fetch_time}\n"
    f"Open Price: {open_price}\n"
    f"Close Price: {close_price}\n"
    f"Percentage Change: {percentage_change:.2f}%\n"
)

# Save to a file in the same directory as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "stock_data.txt")
with open(file_path, "w") as file:
    file.write(result)

# Print the results (for confirmation)
print(result)