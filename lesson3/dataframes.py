import os
import pandas as pd
import matplotlib.pyplot as plt

def get_dataframe_symbol(symbol, base_dir="../data"):
    path = os.path.join(base_dir, "{}.csv".format(symbol))
    df = pd.read_csv(path, index_col="Date", parse_dates=True,
                     usecols=["Date", "Adj Close"], na_values=["nan"])
    return df

def test_run():
    start_date = "2017-01-01"
    end_date = "2017-12-31"
    dates = pd.date_range(start_date, end_date)
    df = pd.DataFrame(index=dates)

    #APLE dataframe
    dfAPPLE = get_dataframe_symbol("AAPL")
    #df = df.join(dfAPPLE)
    #drop NaN
    #df = df.dropna()

    df = df.join(dfAPPLE, how="inner")

    print df


def loadDataFrame(symbols):
    start_date = "2017-01-01"
    end_date = "2017-12-31"
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

#test_run()
symbols = ["SPY", "AAPL", "AMZN", "GOOG", "IBM"]
df = loadDataFrame(symbols)
#print df
#print df.ix["2017-02-01":"2017-02-28"]
#print df[["GOOG", "SPY"]]
#print df.ix["2017-02-01":"2017-02-28", ["SPY", "GOOG"]]

df = normalize_data(df)
plot_selected(df, ['SPY', 'IBM'], '2017-01-01', '2017-04-01')