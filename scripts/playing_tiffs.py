import os
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import imageio as im

tiff_file = '/Users/atredenn/Downloads/modis-250-gpp-2001001.tif'
raster = im.imread(tiff_file)
raster.shape
raster2 = raster[0:,0:,1]

ndv = np.amax(raster2)

plt.imshow(raster2)
plt.colorbar()