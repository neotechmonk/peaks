

from chart import PLOT_STYLE, additional_plot_factory, draw_chart
from data import sample_6M_daily_price
from lib.scipy_signal_find_peaks_cwt import find_peaks


def draw_peaks(ticker: str, peak_finder_fn, *peak_finder_fn_args, **peak_finder_fn_kwargs):
    data = sample_6M_daily_price(ticker="AAPL")
    addplots =[]

    scipy_cwt_peaks = peak_finder_fn(data['High'], *peak_finder_fn_args, **peak_finder_fn_kwargs)
    addplots.append(additional_plot_factory(additional_plot_data=scipy_cwt_peaks,
                                             additional_plot_style=PLOT_STYLE.DOWN_MARKER,
                                             label="scipy_cwt_peaks"))


    fig = draw_chart(data, addplots, {'title':f"{ticker} -{peak_finder_fn.__module__}.{peak_finder_fn.__name__}"}, returnfig=False)
    fig.show()


def main():
    draw_peaks(ticker='MSFT', peak_finder_fn=find_peaks, widths=None, max_distances=None)
    

if __name__ =="__main__":
    # main_single()
    main()