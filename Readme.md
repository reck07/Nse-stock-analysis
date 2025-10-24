NSE VWAP & Volume Spike Checker

This small Python script checks the last 30 minutes of today’s trading (3:00 PM to 3:30 PM) for any big volume spikes in an NSE stock. It also calculates VWAP for this time period. Useful to see if big traders jumped in late.

What you need
• Python installed
• Internet connection
• These Python packages:

pip install yfinance pandas
How to use
Open the script nse_volume_spike.py

Change the stock symbol if you want
Example: symbol = "HDFCBANK"

Run the file from Command Prompt:

python nse_volume_spike.py
Best time to run
After 3:30 PM IST, when the full data for today is available.
