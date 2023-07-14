
from abc import ABC
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, TypeVar

import mplfinance as mpf
import numpy as np
import pandas as pd

PriceData = TypeVar('PriceData', np.ndarray, List, pd.DataFrame)


def draw_chart(data: PriceData, 
               addplots: List[Dict[str, Any]] = None, 
               plot_settings: Dict[str, Any] = None, 
               returnfig = False) -> Any:
    """
    Function to draw a chart with optional inputs
        - additional plots (as a list of dictionaries)
        - plot_settings

    Params: 
        @returnfig = returns the fig instead of plotting/showing the chart 
    """
    plot_params = plot_settings.copy() if plot_settings else {}

    if addplots is not None:
        plot_params["addplot"] = addplots

    fig,_ = mpf.plot(data=data, **plot_params,returnfig=returnfig)
    
    return fig


#######################
# related additional plots
# Used in mplfinance.make_addplot()
#######################

@dataclass  
class PlotStyle(ABC):
    ylabel: str 
    type:str
    color:str

    def __new__(cls, *args, **kwargs):
        if cls is PlotStyle:
            raise TypeError("PlotStyle class is abstract and cannot be instantiated directly.")
        return super().__new__(cls)

@dataclass
class LineStyle(PlotStyle):
    type: str = 'line'
    color: str = 'blue'
    

@dataclass
class DownMarkerStyle(PlotStyle):
    type: str = 'scatter'
    color: str = 'red'
    marker: str =  'v'
    markersize : int = 50 

@dataclass
class UpMarkerStyle(PlotStyle):
    type: str = 'scatter'
    color: str = 'green'
    marker: str =  '^'
    markersize : int = 50 



AdditionalPlotInput = Callable[[PriceData, PlotStyle], Dict[str, Any]]

def create_additional_plot(add_plot_input: AdditionalPlotInput) -> Any:
    data, plot_style = add_plot_input
    return mpf.make_addplot(data, **plot_style.__dict__)