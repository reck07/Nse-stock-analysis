# 29950.
# 37950.
import yfinance as yf
import pandas as pd
from datetime import time

# Select your stock here
symbol = "RELIANCE"  

def fetch_data():
    # Fetch today's 1-minute intraday data
    stock = yf.Ticker(symbol + ".NS")
    df = stock.history(period="1d", interval="1m")
    df.reset_index(inplace=True)
    df["Datetime"] = pd.to_datetime(df["Datetime"])
    return df

def analyze_spikes(df):
    start = time(15, 0)
    end = time(15, 30)

    # Filter last 30 minutes
    df_last_30 = df[(df["Datetime"].dt.time >= start) &
                    (df["Datetime"].dt.time <= end)]

    if df_last_30.empty:
        print("No data found for the timeframe.")
        return

    # VWAP calculation
    vwap = (df_last_30["Close"] * df_last_30["Volume"]).sum() / df_last_30["Volume"].sum()

    spikes = []
    for i in range(5, len(df_last_30)):
        current_vol = df_last_30.iloc[i]["Volume"]
        previous_avg = df_last_30.iloc[i-5:i]["Volume"].mean()

        if previous_avg > 0 and current_vol >= 2 * previous_avg:
            prev_price = df_last_30.iloc[i-5]["Close"]
            curr_price = df_last_30.iloc[i]["Close"]
            change = (curr_price - prev_price) / prev_price * 100

            if change > 0.2:
                move = "increase"
            elif change < -0.2:
                move = "decrease"
            else:
                move = "constant"

            spikes.append({
                "time": df_last_30.iloc[i]["Datetime"].strftime("%H:%M:%S"),
                "volume": int(current_vol),
                "price_change": move
            })

    # Print output
    print("\n VWAP in last 30 minutes:", round(vwap, 2))
    print("Volume Spikes Found:")
    print(spikes)

if __name__ == "__main__":
    df = fetch_data()
    analyze_spikes(df)







