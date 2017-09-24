import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("../data/AAPL.csv")
    print "HEAD"
    print df.head(5)
    print "TAIL"
    print df.tail(5)

def printRows(start, n):
    df = pd.read_csv("../data/AAPL.csv")
    end = start + n
    print df[start:end]

def maxClose():
    df = pd.read_csv("../data/AAPL.csv")
    print df["Close"].max()


def get_max_close_symbol(symbol):
    df = pd.read_csv("../data/{}.csv".format(symbol))
    return df["Close"].max()

def get_mean_symbol(symbol):
    df = pd.read_csv("../data/{}.csv".format(symbol))
    return df["Close"].mean()

def plotHighPrices(symbol):
    df = pd.read_csv("../data/{}.csv".format(symbol))
    df["High"].plot()
    plt.title("{} high prices".format(symbol))
    plt.xlabel("time")
    plt.ylabel("$")
    plt.grid(True)
    plt.show()


def plotHigh_Adjacent(symbol):
    df = pd.read_csv("../data/{}.csv".format(symbol))
    df[["High","Adj Close"]].plot()
    plt.title("{} high and adj close".format(symbol))
    plt.xlabel("time")
    plt.ylabel("$")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    symbols = ["AAPL","AMZN", "GOOG", "IBM", "T", "VZ"]
    #for symbol in symbols:
    #    print "Mean"
    #    print symbol, get_mean_symbol(symbol)
    print plotHigh_Adjacent("IBM")