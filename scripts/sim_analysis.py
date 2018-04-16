"""
This script generates fake raster data to simulate the analysis
we will have to do in the cloud. This tests the general algorithm
and workflow.

Author: Andrew Tredennick (atredenn@gmail.com)
"""

import numpy as np
import matplotlib as plt

# Make a big time series of 'rasters', here a numpy array
nyears = 5
nrows = 100
ncols = 100
start_matrix = np.random.lognormal(mean = np.log(0.1), sigma = np.log(1.5), size = (nrows, ncols))

# Define a simple AR(1) process function
def generate_ar1 (mat, ntimes, beta = 0.8):
    '''Just a little function to simulate an AR(1) process
    
    Args:
        mat: a 2D numpy.ndarray
        ntimes: the number of iterations for the process
        beta: the autoregression parameter
    
    Returns:
        the_array: a 3D array with size = (mat.shape[0], mat.shape[1], ntimes)
            representing a time-evolving spatial field
    '''
    do_cols = mat.shape[1]
    do_rows = mat.shape[0]
    the_array = np.zeros(shape = (do_rows, do_cols, ntimes))
    the_array[:,:,0] = mat # set first year to mat
    
    for t in range(1,ntimes):
        the_array[:,:,t] = the_array[:,:,t-1]*beta + np.random.normal(0,1,size = mat.shape)
    
    return the_array

# Now get the time series
data_mat = generate_ar1(start_matrix, nyears, 0.8)

# Define a function for calculating temporal variance, 
# given a spatial scale


    





