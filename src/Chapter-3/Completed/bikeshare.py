import pint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import json
from os.path import join


def flip(p=0.5):
    """Flips a coin with the given probability.

    p: float 0-1

    returns: boolean (True or False)
    """
    return np.random.random() < p

def decorate(**options):
    """Decorate the current axes.

    Call decorate with keyword arguments like
    decorate(title='Title',
             xlabel='x',
             ylabel='y')

    The keyword arguments can be any of the axis properties
    https://matplotlib.org/api/axes_api.html
    """
    ax = plt.gca()
    ax.set(**options)

    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(handles, labels)

    plt.tight_layout()

def State(**variables):
    """Contains the values of state variables."""
    return pd.Series(variables, name='state')

def bike_to_wellesley(bikeshare):
    """
    """
    if bikeshare.olin == 0:
#         print('0 bike to move')
        return
    else:
#         print('Moving a bike to Wellesley')
        bikeshare.olin -= 1
        bikeshare.wellesley += 1

def bike_to_olin(bikeshare):
    """
    """
    if bikeshare.wellesley == 0:
#         print('0 bike to move')
        return
    else:
#         print('Moving a bike to Olin')
        bikeshare.olin += 1
        bikeshare.wellesley -= 1

def step(bikeshare, p1, p2):
    """
    """
    if flip(p1):
        bike_to_wellesley(bikeshare)
    
    if flip(p2):
        bike_to_olin(bikeshare)

def TimeSeries(*args, **kwargs):
    """
    """
    if args or kwargs:
        series = pd.Series(*args, **kwargs)
    else:
        series = pd.Series([], dtype=np.float64)

    series.index.name = 'Time'
    if 'name' not in kwargs:
        series.name = 'Quantity'
    return series

def run_simulation(bikeshare, p1, p2, num_steps):
    """
    """
    results = TimeSeries()
    for i in range(num_steps):
        step(bikeshare, p1, p2)
        results[i] = bikeshare.olin
    return results

def display_results(results):
    """
    """
    result_graph = results.plot()
    decorate(title = 'Olin-Wellesley Bikeshare System',
            xlabel = 'Time stop (min)',
            ylabel = 'Number of bikes')
    result_fig = result_graph.get_figure()
    return result_fig