'''Chart module for creating interactive chart.'''
 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def set_default_theme(style='darkgrid', **kwargs):
    '''Set the aesthetic style of the plots.
    Args:
        style (str): darkgrid, darkgrid, dark, white, ticks
        kwargs: Additional parameters to control the aesthetics of the grid.'''
    sns.set_theme(style=style, **kwargs)

def scatter_plot(data, x, y, hue= None, **kwargs):
    '''Plot data and regression model fits across a FacetGrid.
    Args:
        data (DataFrame): CSV file path or DataFrame object.
        x, y (str): Variables that specify positions on the x and y axes.
        hue (str): Variable in data to map plot aspects to different colors.
        kwargs: Additional keyword arguments are passed to the function used to draw the plot on the joint Axes, superseding items in the joint_kws dictionary.
    '''
    if isinstance(data, str):
        df = pd.read_csv(data)
    else:
        df = data
    sns.catplot(data=df, x=x, y=y, hue=hue, **kwargs)

def violin_plot(data, x, y, hue= None, **kwargs):
    '''Plot data and regression model fits across a FacetGrid.
    Args:
        data (DataFrame): CSV file path or DataFrame object.
        x, y (str): Variables that specify positions on the x and y axes.
        hue (str): Variable in data to map plot aspects to different colors.
        kwargs: Additional keyword arguments are passed to the function used to draw the plot on the joint Axes, superseding items in the joint_kws dictionary.
    '''
    if isinstance(data, str):
        df = pd.read_csv(data)
    else:
        df = data
    sns.violinplot(data=df, x=x, y=y, hue=hue, **kwargs)

def violin_spilt(data, x, y, hue, spilt= True, **kwargs):
    '''Plot data and regression model fits across a FacetGrid.
    Args:
        data (DataFrame): CSV file path or DataFrame object.
        x, y (str): Variables that specify positions on the x and y axes.
        hue (str): Variable in data to map plot aspects to different colors.
        spilt (bool): Whether to draw half of a violin for each hue level or allow them to overlap.
        kwargs: Additional keyword arguments are passed to the function used to draw the plot on the joint Axes, superseding items in the joint_kws dictionary.
    '''
    if isinstance(data, str):
        df = pd.read_csv(data)
    else:
        df = data
    sns.violinplot(data=df, x=x, y=y, hue=hue, split=spilt, **kwargs)

def single_violin(data, variable, **kwargs):
    '''Plot data and regression model fits across a FacetGrid.
    Args:
        data (DataFrame): CSV file path or DataFrame object.
        variable (str): Variables that specify positions on the x and y axes.
        kwargs: Additional keyword arguments are passed to the function used to draw the plot on the joint Axes, superseding items in the joint_kws dictionary.
    '''
    if isinstance(data, str):
        df = pd.read_csv(data)
    else:
        df = data
    sns.violinplot(x=df[variable], **kwargs)

def box_plot(data, x, y, hue= None, **kwargs):
    '''Plot data and regression model fits across a FacetGrid.
    Args:
        data (DataFrame): CSV file path or DataFrame object.
        x, y (str): Variables that specify positions on the x and y axes.
        hue (str): Variable in data to map plot aspects to different colors.
        kwargs: Additional keyword arguments are passed to the function used to draw the plot on the joint Axes, superseding items in the joint_kws dictionary.
    '''
    if isinstance(data, str):
        df = pd.read_csv(data)
    else:
        df = data
    sns.boxplot(data=df, x=x, y=y, hue=hue, **kwargs)

def single_box_plot(data, variable, **kwargs):
    '''Plot data and regression model fits across a FacetGrid.
    Aegs:
        data (DataFrame): CSV file path or DataFrame object.
        variable (str): Variables that specify positions on the x and y axes.
        kwargs: Additional keyword arguments are passed to the function used to draw the plot on the joint Axes, superseding items in the joint_kws dictionary.
    '''
    if isinstance(data, str):
        df = pd.read_csv(data)
    else:
        df = data
    sns.boxplot(data=df,x=df[variable], **kwargs)

