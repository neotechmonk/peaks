from functools import cache

from chart import draw_chart
from data import sample_6M_daily_price


def main():
    
    data= sample_6M_daily_price(ticker="AAPL")
    # print(data)
    fig = draw_chart(data)
    fig.show()

if __name__ =="__main__":
    main()