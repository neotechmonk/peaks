# quantX
Proof of concept for algorithmic trading using python


# TODO 
1. Ovelay value add - indicators, signals (modular functions)
    1. SMA - fast, medium, slow [TT] 20230703
    1. RSI 
    1. Bollinger
    1. Zig Zag
    1. Arrows and pointers
1. TV like aesthetics
1. Multiple instruments - static [RM] 20230703

# How to setup developer environment
1. Clone the remote repository `https://github.com/neotechmonk/quantX.git` and `cd quantX` 
1. Setup the virtual environment
    * `python -m venv venv` 
    * `source venv/bin/activate`
        * [Virtual environements in Windows](https://docs.python.org/3/library/venv.html)
1. Install package dependencies - `pip install -r requirements.txt`
1. Run the app - `python src/app.py`

# Project organisation
*  code base folder
    * `src` - program 
    * `tests` - tests
* `app.py` is the entry point for the program
* `gui` package - presentation layer in `tkinter`
* `chart` package - charting using `mplfinance`
* `ticker` package - popup and associated files to dynamically select tickers  ```TODO: move to appriate packages, e.g. gui?```


# Packages used
* [`pandas`](https://pypi.org/project/pandas/), [`numpy`](https://pypi.org/project/numpy/) - vectorised manipulation of price data
* [`ta`](https://pypi.org/project/ta/) - out of the box Technical Analysis Indicators
* [`yfinance`](https://pypi.org/project/yfinance/) - price data
* [`pytest`](https://docs.pytest.org/) - test automation. Not implemeted as of 20230711

