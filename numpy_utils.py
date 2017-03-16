"""
Utilities for working with numpy arrays
"""

import numpy
import pandas

def summarize(np_array):
    """Summarize the values in a numpy array, treating it as 1-d"""

    series = pandas.Series(np_array.ravel())
    print(series.describe())

def unmasked_logical(ma_array):
    """Given a masked array (numpy.ma) of logicals, convert it to an unmasked
    array by changing fill value to False"""

    return ma_array.filled(False)
