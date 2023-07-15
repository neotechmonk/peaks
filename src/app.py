from functools import cache

from chart import additional_plot_factory as addplot_factory
from chart import draw_chart
from data import sample_6M_daily_price


def main_single():
    data = sample_6M_daily_price(ticker="AAPL")
    add_plotdata = data["Close"] * 2

    add_plots=[]
    add_plots.append(additional_plot_factory(additional_plot_data=add_plotdata,
                                             additional_plot_style='line',
                                             label="Double Close"))
    # line_style = PlotStyle(ylabel='signal', type='line', color='purple')

    fig = draw_chart(data, add_plots, {'title':"GRAND CHART"})
    fig.show()


def main_multi():
    data = sample_6M_daily_price(ticker="AAPL")

    addplots =[]

    addplot_data1 = data["Close"] * 2
    addplots.append(addplot_factory(additional_plot_data=addplot_data1,
                                             additional_plot_style='line',
                                             label="Double Close"))

    addplot_data2 = data["Close"] * 1.5 
    addplots.append(addplot_factory(additional_plot_data=addplot_data2,
                                             additional_plot_style='up_marker',
                                             label="Double Close"))


    # line_style = PlotStyle(ylabel='signal', type='line', color='purple')

    fig = draw_chart(data, addplots, {'title':"GRAND CHART"})
    fig.show()

if __name__ =="__main__":
    # main_single()
    main_multi()