A Python script that analyzes a stock portfolio and runs a Monte Carlo price simulation.

--Features--
- Calculates total portfolio value
- Identifies the largest and smallest positions
- Calculates profit and loss for each ticker
- Calculates portfolio weights
- Measures historical price volatility
- Simulates 10,000 possible one-year price paths
- Displays portfolio and simulation charts

--Files--

- `codeful.py` — main analysis and simulation script

- `holdings.csv` — shares owned and cost basis

- `current_prices.csv` — current prices for each ticker

- `prices.csv` — historical closing prices

--Requirements--

- pandas
- NumPy
- Matplotlib
--------------------
The CSV files must be in the same folder as `codeful.py`.

--CSV FILES--

** current_prices.csv **
  ticker,price
  
  AAPL,180
  
  TSLA,250
  
  NVDA,12
  
** prices.csv **
  date,close
  
  2026-01-02,100
  
  2026-01-03,103
  
  2026-01-04,101
  
  
** holdings.csv **

  ticker,shares,cost_basis
  
  AAPL,10,150
  
  TSLA,5,300
  
  NVDA,8,100
  


-----Disclaimer-----
This project is for educational purposes only. It is not financial advice, and the simulations do not predict actual market performance.
