from functools import cache

from chart import (DownMarkerStyle, LineStyle, UpMarkerStyle,
                   create_additional_plot, draw_chart)
from data import sample_6M_daily_price


def main():
    data = sample_6M_daily_price(ticker="AAPL")
    add_plotdata = data["Close"] * 2

    line_style = UpMarkerStyle(ylabel='signal')

    add_plot_input = (add_plotdata, line_style)

    fig = draw_chart(data, create_additional_plot(add_plot_input))
    fig.show()

if __name__ =="__main__":
    main()