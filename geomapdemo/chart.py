import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''Since many of the GIS spatial analysis involve the use of charts,
 I recommend the chart section in geomapdemo package, 
 which based on the seaborn to make people convenient to generate the charts.'''


def set_default_theme(style='darkgrid', **kwargs):
    '''Set the aesthetic style of the plots.
    Args:
        style (str): darkgrid, darkgrid, dark, white, ticks
        kwargs: Additional parameters to control the aesthetics of the grid.'''
    sns.set_theme(style=style, **kwargs)

def scatter_plot(data, x, y, **kwargs):
    '''Plot data and regression model fits across a FacetGrid.
    Args:
        data (DataFrame): CSV file path or DataFrame object.
        x, y (str): Variables that specify positions on the x and y axes.
        kwargs: Additional keyword arguments are passed to the function used to draw the plot on the joint Axes, superseding items in the joint_kws dictionary.
    '''
    if isinstance(data, str):
        df = pd.read_csv(data)
    else:
        df = data
    sns.catplot(data=df, x=x, y=y, **kwargs)

