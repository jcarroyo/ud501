import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_dataframe_symbol(symbol, base_dir="../data"):
    path = os.path.join(base_dir, "{}.csv".format(symbol))
    df = pd.read_csv(path, index_col="Date", parse_dates=True,
                     usecols=["Date", "Adj Close"], na_values=["nan"])
    return df

def loadDataFrame(symbols, start_date, end_date):
    dates = pd.date_range(start_date, end_date)
    df = pd.DataFrame(index=dates)
    for s in symbols:
        df_temp = get_dataframe_symbol(s)
        df_temp = df_temp.rename(columns={"Adj Close": s})
        df = df.join(df_temp, how="inner")
    return df

def plot_data(df, title="Stock Prices"):
    p = df.plot(title=title)
    p.set_xlabel("Date")
    p.set_ylabel("Price")
    plt.show()

def normalize_data(df):
    return df / df.ix[0,:]

def plot_selected(df, columns, start_index, end_index):
    df_aux = df.ix[start_index:end_index, columns]
    plot_data(df_aux)

def test_run():
    start_date = "2017-01-01"
    end_date = "2017-12-31"
    symbols = ["SPY", "AAPL", "AMZN", "GOOG", "IBM"]

    df = loadDataFrame(symbols, start_date, end_date)
    plot_data(df)
    print "MEAN\n", df.mean()
    print "MEDIAN\n", df.median()
    print "SD\n", df.std()


def get_rolling_mean(values, window):
    rolling = pd.rolling_mean(values, window=window)
    return rolling

def get_rolling_std(values, window):
    rolling = pd.rolling_std(values, window=window)
    return rolling

def get_bollinger_bands(rm, rstd):
    upper_band = np.add(rm, rstd*2)
    lower_band = np.subtract(rm, rstd*2)
    return upper_band, lower_band

def rolling_statistics():
    start_date = "2017-01-01"
    end_date = "2017-12-31"
    symbols = ["SPY"]
    df = loadDataFrame(symbols, start_date, end_date)

    #Rolling Mean
    rolling_mean = get_rolling_mean(df["SPY"], 20)
    #Rolling Standard Deviation
    rolling_std = get_rolling_std(df["SPY"], 20)
    #Bollinger Bands
    upper_band, lower_band = get_bollinger_bands(rolling_mean, rolling_std)

    #Plot raw SPY
    ax = df["SPY"].plot(title="Bollinger Bands", label="SPY")

    rolling_mean.plot(label="Rolling Mean", ax=ax)
    upper_band.plot(label="Upper band", ax=ax)
    lower_band.plot(label="Lower band", ax=ax)

    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc="upper left")
    plt.show()


def compute_daily_return(df):
    #Daily return formula
    # daily_return[t] = (price[t] / price[t-1]) - 1

    #daily_returns = df.copy()
    #daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    #daily_returns.ix[0,:] = 0

    #With Pandas
    daily_returns = (df / df.shift(1)) - 1
    daily_returns.ix[0, :] = 0
    return daily_returns

def compute_cumulative_return(df):
    #Cumulative return formula
    # cumret[t] = (price[t] / price[0]) - 1
    cumulative_returns = df.copy()
    cumulative_returns = (df[1:] / df.ix[0]) - 1
    cumulative_returns.ix[0,:] = 0
    return cumulative_returns


def daily_return():
    start_date = "2017-01-01"
    end_date = "2017-12-31"
    symbols = ["T", "VZ"]
    df = loadDataFrame(symbols, start_date, end_date)
    df_daily_return = compute_daily_return(df)
    plot_data(df_daily_return, title="Daily Return")

def cumulative_return():
    start_date = "2017-01-01"
    end_date = "2017-12-31"
    symbols = ["T", "VZ"]
    df = loadDataFrame(symbols, start_date, end_date)
    df_cumr = compute_cumulative_return(df)
    plot_data(df_cumr, title="Daily Return")

if __name__ == "__main__":
    cumulative_return()