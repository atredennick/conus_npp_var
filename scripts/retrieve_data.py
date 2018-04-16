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
#base_url = "http://files.ntsg.umt.edu/data/Landsat_Productivity/landsat-30-npp/"
#base_fname = "landsat-30-npp-"
#years = map(str, range(1986,2018)) # list of years, as strings

# For MODIS
base_url = "http://files.ntsg.umt.edu/data/NTSG_Products/MOD17/MODIS_250/modis-250-npp/"
base_fname = "modis-250-npp-"
years = map(str, range(2001,2018)) # list of years, as strings

# Generic
fname_ext = ".tif"
out_dir = "../data/"

# # Put all fnames together
# fnames_tmp = [base_fname + years for years in years] # append base name to each year
# fnames = [fnames_tmp + fname_ext for fnames_tmp in fnames_tmp] # append ftype to each fname

# # Loop over files, download, and save
# for dofile in fnames[0:1]:
#     out_file = out_dir + dofile
#     read_url = base_url + dofile
#     #print(read_url)
#     urllib.urlretrieve(read_url, out_file, reporthook)
    
