"""
This script loops through all the NPP .tif files and downloads them
into the data directory. This will take a while; each file is 24 GB.

UPDATE: In fact, this just isn't tractable, will have to do all
analysis in the cloud.
"""
import sys
import time
import urllib
import os 

# Choose a satellite
do_satellite = "MODIS"

# A little function for reporting download progress
def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                    (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()

# For Landsat
if do_satellite == "Landsat":
    base_url = "http://files.ntsg.umt.edu/data/Landsat_Productivity/landsat-30-npp/"
    base_fname = "landsat-30-npp-"
    years = map(str, range(1986,2018)) # list of years, as strings

# For MODIS
if do_satellite == "MODIS":
    base_url = "http://files.ntsg.umt.edu/data/NTSG_Products/MOD17/MODIS_250/modis-250-npp/"
    base_fname = "modis-250-npp-"
    years = map(str, range(2001,2018)) # list of years, as strings

# Generic data stuff
fname_ext = ".tif"
out_dir = "../data/"

# Create out_dir if it doesn't exist
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

# Put all fnames together
fnames_tmp = [base_fname + years for years in years] # append base name to each year
fnames = [fnames_tmp + fname_ext for fnames_tmp in fnames_tmp] # append ftype to each fname

# Loop over files, download, and save
for dofile in fnames[0:7]:
    out_file = out_dir + dofile
    read_url = base_url + dofile
    urllib.urlretrieve(read_url, out_file, reporthook)








# ## For reading in chunks...
# import gdal
# ds = gdal.Open('input.tif', gdal.GA_ReadOnly)
# rb = ds.GetRasterBand(1)
# xsize = rb.XSize
# ysize = rb.YSize
# ystep = ysize / 10
# yresidual = ysize - (ystep * 10)

# for i in range(10):
#     if i != 9:
#         img_part = rb.ReadAsArray(0, ystep * i, xsize, ystep)
#     else:
#         img_part = rb.ReadAsArray(0, ystep * i, xsize, ystep + yresidual)
#     # do something with img_part

# ds = None
    
