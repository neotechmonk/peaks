
from typing import Any, Dict, List

import mplfinance as mpf
import pandas as pd


def draw_chart(data: pd.DataFrame, addplots: List[Dict[str, Any]] = None, plot_settings: Dict[str, Any] = None) -> Any:
    """
    Function to draw a chart with optional inputs
        - additional plots (as a list of dictionaries)
        - plot_settings
    """
    plot_params = plot_settings.copy() if plot_settings else {}

    if addplots is not None:
        plot_params["addplot"] = addplots

    fig, _ = mpf.plot(data=data, **plot_params)

    return fig
