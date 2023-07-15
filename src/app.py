

import numpy as np

from chart import PLOT_STYLE, additional_plot_factory, draw_chart
from data import sample_6M_daily_price
from lib.peaks import scipy_signal_find_peaks_cwt


def draw_peaks(ticker: str, peak_finder_fn, *peak_finder_fn_args, **peak_finder_fn_kwargs):
    
    data = sample_6M_daily_price(ticker=ticker)

    input_vector  = data['High']
    peaks = peak_finder_fn(input_vector, *peak_finder_fn_args, **peak_finder_fn_kwargs)
    
    result = np.full_like(input_vector, np.nan)
    result[peaks] = input_vector[peaks]

    addplots =[]
    addplots.append(additional_plot_factory(additional_plot_data=result,
                                             additional_plot_style=PLOT_STYLE.DOWN_MARKER
                                            )
                    )

    draw_chart(data, 
                     addplots, 
                     {'title':f"{ticker} - {peak_finder_fn.__module__}.{peak_finder_fn.__name__}"},
                    returnfig=False)
    


def main(ticker):
    draw_peaks(ticker=ticker, peak_finder_fn=scipy_signal_find_peaks_cwt, widths=np.arange(1,4), max_distances=np.arange(1,4))
    draw_peaks(ticker=ticker, peak_finder_fn=scipy_signal_find_peaks_cwt, widths=np.arange(1,4), max_distances=np.arange(1,4))
   

if __name__ =="__main__":
    main("MSFT")