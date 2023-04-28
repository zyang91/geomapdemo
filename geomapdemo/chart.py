import pandas as pd
import seaborn as sns

'''Since many of the GIS spatial analysis involve the use of charts,
 I recommend the chart section in geomapdemo package, 
 which based on the seaborn to make people convenient to generate the charts.'''


def set_theme(style='darkgrid', **kwargs):
    '''Set the aesthetic style of the plots.
    Args:
        style (str): darkgrid, darkgrid, dark, white, ticks
        kwargs: Additional parameters to control the aesthetics of the grid.'''
    sns.set_theme(style=style, **kwargs)

