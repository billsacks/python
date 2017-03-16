import numpy
import pandas

def summarize(np_array):
    """Summarize the values in a numpy array, treating it as 1-d"""

    series = pandas.Series(np_array.ravel())
    print(series.describe())

