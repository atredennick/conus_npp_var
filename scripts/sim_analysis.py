"""
This script generates fake raster data to simulate the analysis
we will have to do in the cloud. This tests the general algorithm
and workflow.

Author: Andrew Tredennick (atredenn@gmail.com)
"""

import numpy as np
import matplotlib as plt
import scipy as sp
import skimage

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
    assert mat.ndim == 2, 'mat is not a 2D array'
    
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
def shrink(data, rows, cols):
    return data.reshape(rows, data.shape[0]/rows, cols, data.shape[1]/cols).sum(axis=1).sum(axis=2)

def calc_variance (array, factor = 1):
    assert array.ndim == 3, 'array_obj is not a 3D array'
    # TODO: test that factor one cause errors for shrinking array
    
    if factor == 1:
        out_var = np.var(array, axis = 2)
    
    if factor != 1: 
        new_array = np.zeros(shape = (array.shape[0]/factor, array.shape[1]/factor, array.shape[2]))
        
        for i in range(array.shape[2]):
            tmp_array = array[:,:,i]
            new_array[:,:,i] = shrink(tmp_array, tmp_array.shape[0]/factor, tmp_array.shape[1]/factor)
        
        out_var = np.var(new_array, axis = 2)
    
    return out_var

# Test and plot real quick
plt.pyplot.imshow(calc_variance(data_mat, factor = 5))
