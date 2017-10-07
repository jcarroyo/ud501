import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_dataframe_symbol(symbol, base_dir="../data"):
    path = os.path.join(base_dir, "{}.csv".format(symbol))
    if(not os.path.isfile(path)):
        msg = "File " + path + " does not exist"
        raise Exception(msg)
    df = pd.read_csv(path, index_col="Date", parse_dates=True,
                     usecols=["Date", "Adj Close"], na_values=["nan"])
    return df

def loadDataFrame(symbols, start_date, end_date):
    dates = pd.date_range(start_date, end_date)
    df = pd.DataFrame(index=dates)
    if "SPY" not in symbols:
        symbols.insert(0, "SPY")

    for s in symbols:
        df_temp = get_dataframe_symbol(s)
        df_temp = df_temp.rename(columns={"Adj Close": s})
        df = df.join(df_temp)
        if s == "SPY":
            df = df.dropna(subset=["SPY"])
    return df

def fill_missing_values(df):
    df.fillna(method="ffill", inplace=True)
    df.fillna(method="backfill", inplace=True)
    return df

def plot_data(df, title="Stock Prices"):
    p = df.plot(title=title)
    p.set_xlabel("Date")
    p.set_ylabel("Price")
    plt.show()

def test():
    start_date = "2017-01-01"
    end_date = "2017-12-31"
    symbols = ["SPY", "FAKE1", "FAKE2"]
    df = loadDataFrame(symbols, start_date, end_date)
    df = fill_missing_values(df)
    plot_data(df, title="fillna")

if __name__ == "__main__":
    test()