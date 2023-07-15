
from abc import ABC
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Dict, List, TypeVar

import mplfinance as mpf
import numpy as np
import pandas as pd

__all__ = ['additional_plot_factory', 'draw_chart', 'PLOT_STYLE']

###################################
# related to additional plots
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



class PLOT_STYLE(Enum):
    LINE = LineStyle
    UP_MARKER = UpMarkerStyle
    DOWN_MARKER = DownMarkerStyle

###################################
# Chart with additional plots
###################################


#Permitted data types of price feed
PriceData = TypeVar('PriceData', np.ndarray, List, pd.DataFrame)

#structural type addtioan plot creation function
AdditionalPlotCreator = Callable[[PriceData, PlotStyle], Dict[str, Any]]
def __create_additional_plot(add_plot_input: AdditionalPlotCreator) -> Dict[str, Any]:
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
def additional_plot_factory(additional_plot_data:PriceData, 
                            additional_plot_style:PLOT_STYLE, 
                            label:str ="", 
                            additional_plot_creator_fn = __create_additional_plot)-> AdditionalPlotCreator:
    """
    Params
        label :  y_axis label for the additional plot
    """
    plot_style = additional_plot_style.value(ylabel=label)
    
    return additional_plot_creator_fn((additional_plot_data, plot_style))
    