import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
start=100
mu=0.001
sigma=0.02
days=252
n_paths=10000
def load_portfolio():
    df = pd.read_csv("holdings.csv")
    df_prices = pd.read_csv("current_prices.csv")
    merged = df.merge(df_prices, on="ticker")
    return merged
def load_prices():
    df = pd.read_csv("prices.csv")
    return df
def add_portfolio_columns(merged):
    merged["value"]= merged["shares"]*merged["price"]
    merged["return"] = (merged["price"] - merged["cost_basis"]) / merged["cost_basis"]
    merged["pnl"] = (merged["price"] - merged["cost_basis"]) * merged["shares"]
    merged["weight"] = (merged["value"] / merged["value"].sum())
    return merged

def volatility(df):
    df["return"] = df["close"].pct_change()
    vol = df["return"].std(ddof=0)
    return vol

def simulate(start, mu, sigma, days, n_paths):
    np.random.seed(0)
    daily2darray = np.random.normal(mu,sigma,(days,n_paths))
    paths = start * (1 + daily2darray).cumprod(axis=0)
    return paths
def print_summary(merged, vol, paths, start):
    print(f"Your total value is {merged['value'].sum()}")
    print(f"Your biggest position is {merged.loc[merged['value'].idxmax(), 'ticker']} with a value of {merged['value'].max()}")
    print(f"Your smallest position is {merged.loc[merged['value'].idxmin(), 'ticker']} with a value of {merged['value'].min()}")
    print(f"Your total pnl is {merged["pnl"].sum()}")
    print(f"Volatility : {vol}")
    final = paths[-1]
    below = len(final[final < start])
    print(f"Prices below start : {below / len(final)}")
    print(f"Mean : {final.mean()}")
    print(f"Median : {np.median(final)}")
    print(f"5th percentile : {np.percentile(final, 5)}")
    print(f"95th percentile : {np.percentile(final, 95)}")
def chart_pnl(merged):
    colors = []
    for x in merged["pnl"]:
        if x > 0:
            colors.append("green")
        else:
            colors.append("red")
    plt.bar(merged["ticker"], merged["pnl"],color=colors)
    plt.title("P&L by ticker")
    plt.ylabel("P&L ($)")
    plt.xlabel("Ticker")
    plt.show()
def chart_paths(paths):
    plt.plot(paths[:, :200],alpha=0.3)
    plt.title("200 simulated one year price paths")
    plt.xlabel("Days")
    plt.ylabel("Price ($)")
    plt.show()
def chart_histogram(final,start):
    plt.hist(final, bins=20)
    plt.title("Distribution of ending prices after one year")
    plt.axvline(start, color="red")
    plt.xlabel("Ending price")
    plt.ylabel("Paths")
    plt.show()

def main():
    merged = add_portfolio_columns(load_portfolio())
    vol = volatility(load_prices())
    paths = simulate(start, mu, sigma, days, n_paths)
    print_summary(merged, vol, paths, start)
    chart_paths(paths)
    chart_histogram(paths[-1],start)
    chart_pnl(merged)
if __name__ == "__main__":
    main()
