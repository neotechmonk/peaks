from functools import cache

from chart import (DownMarkerStyle, LineStyle, PlotStyle, UpMarkerStyle,
                   create_additional_plot, draw_chart)
from data import sample_6M_daily_price


def main_single():
    data = sample_6M_daily_price(ticker="AAPL")
    add_plotdata = data["Close"] * 2

    line_style = LineStyle(ylabel='signal')
    # line_style = PlotStyle(ylabel='signal', type='line', color='purple')

    fig = draw_chart(data, create_additional_plot((add_plotdata, line_style)), {'title':"GRAND CHART"})
    fig.show()


def main_multi():
    data = sample_6M_daily_price(ticker="AAPL")

    addplots =[]

    addplot_line1 = data["Close"] * 2
    style_line1 = LineStyle(ylabel='double')
    addplots.append(create_additional_plot((addplot_line1,style_line1)))

    addplot_line2 = data["Close"] * 1.5
    style_line2 = UpMarkerStyle(ylabel='one and half')

    addplots.append(create_additional_plot((addplot_line2,style_line2)))


    # line_style = PlotStyle(ylabel='signal', type='line', color='purple')

    fig = draw_chart(data, addplots, {'title':"GRAND CHART"})
    fig.show()

if __name__ =="__main__":
    # main_single()
    main_multi()