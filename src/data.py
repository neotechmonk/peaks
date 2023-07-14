import datetime
from functools import partial

import pandas as pd
import yfinance as yf


def get_price(ticker : str, start_date : str, end_date : str, interval :str)->pd.DataFrame:
    """
    Params:
        @internal
            '1d': Daily interval (1 day)
            '1wk': Weekly interval (1 week)
            '1mo': Monthly interval (1 month)
            '5m': 5-minute interval
            '15m': 15-minute interval
            '30m': 30-minute interval
            '60m' or '1h': 1-hour interval
            '90m': 90-minute interval
            '1h': 1-hour interval
            '1d': 1-day interval
    """
    return  yf.download(ticker, start=start_date, end=end_date, interval = interval)



# Partial function to return sample data for a given ticker
end_date = datetime.datetime.now().strftime("%Y-%m-%d")
start_date = (datetime.datetime.now() - datetime.timedelta(days=180)).strftime("%Y-%m-%d")

sample_6M_daily_price = partial(get_price,
                                interval='1d', 
                                start_date=start_date, 
                                end_date=end_date)

# print(sample_6M_daily_price(ticker= 'AAPL'))