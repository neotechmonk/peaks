
from abc import ABC
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, TypeVar

import mplfinance as mpf
import numpy as np
import pandas as pd

###################################
# related additional plots
# Used in mplfinance.make_addplot()
###################################

@dataclass  
class PlotStyle(ABC):
    """All attributes are match the dict() paramaters of mplfinance.make_addplot()"""
    ylabel: str 
    type:str
    color:str

    def __new__(cls, *args, **kwargs):
        if cls is PlotStyle:
            raise TypeError(f"{cls.__name__} class is abstract - cannot instantiate")
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

###################################
# Chart with additional plots
###################################


#Permitted data types of price feed
PriceData = TypeVar('PriceData', np.ndarray, List, pd.DataFrame)

#structural type addtioan plot creation function
AdditionalPlotCreator = Callable[[PriceData, PlotStyle], Dict[str, Any]]
def create_additional_plot(add_plot_input: AdditionalPlotCreator) -> Dict[str, Any]:
    data, plot_style = add_plot_input
    return mpf.make_addplot(data, **plot_style.__dict__)


def draw_chart(data: PriceData, 
               addplots: List[AdditionalPlotCreator] = None, 
               plot_settings: Dict[str, Any] = {}, 
               returnfig = False) -> Any:
    """
    Function to draw a chart with optional inputs
        - additional plots (as a list of dictionaries)
        - plot_settings

    Params: 
        @returnfig = returns the fig instead of plotting/showing the chart 
    """

    fig,_ = mpf.plot(data=data, addplot = addplots, **plot_settings,returnfig=returnfig)
    
    return fig

## Factory method to create draw charts with additional plots
# def draw_chart_with_additional_plots(data: