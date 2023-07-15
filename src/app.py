from functools import cache

from chart import PLOT_STYLE, additional_plot_factory, draw_chart
from data import sample_6M_daily_price


def main_single():
    data = sample_6M_daily_price(ticker="AAPL")
    add_plotdata = data["Close"] * 2

    add_plots=[]
    add_plots.append(additional_plot_factory(additional_plot_data=add_plotdata,
                                             additional_plot_style=PLOT_STYLE.LINE,
                                             label="Double Close"))
    # line_style = PlotStyle(ylabel='signal', type='line', color='purple')

    fig = draw_chart(data, add_plots, {'title':"GRAND CHART"})
    fig.show()


def main_multi():
    data = sample_6M_daily_price(ticker="AAPL")

    addplots =[]

    addplot_data1 = data["Close"] * 2
    addplots.append(additional_plot_factory(additional_plot_data=addplot_data1,
                                             additional_plot_style=PLOT_STYLE.LINE,
                                             label="Double Close"))

    addplot_data2 = data["Close"] * 1.5 
    addplots.append(additional_plot_factory(additional_plot_data=addplot_data2,
                                             additional_plot_style=PLOT_STYLE.UP_MARKER,
                                             label="Double Close"))


    # line_style = PlotStyle(ylabel='signal', type='line', color='purple')

    fig = draw_chart(data, addplots, {'title':"GRAND CHART"})
    fig.show()

if __name__ =="__main__":
    # main_single()
    main_multi()