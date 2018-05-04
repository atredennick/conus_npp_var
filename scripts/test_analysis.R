## test_analysis.R: This is a sandbox to see if we can do the IAR analysis
##    in R. Hopefully this script will get ported into a complete analysis.


# Load libraries ----------------------------------------------------------

library(data.table)
library(raster)
library(sp)
library(rgdal)


# Read in data ------------------------------------------------------------

data_dir <- "../data/"
all_files <- list.files(data_dir)
fname <- paste0(data_dir,all_files[1])
test <- raster(fname)



n = 4
mat = matrix(1:n^2, nrow = n)
mat.pad = rbind(NA, cbind(NA, mat, NA), NA)
ind = 2:(n + 1) # row/column indices of the "middle"
neigh = rbind(N  = as.vector(mat.pad[ind - 1, ind    ]),
              NE = as.vector(mat.pad[ind - 1, ind + 1]),
              E  = as.vector(mat.pad[ind    , ind + 1]),
              SE = as.vector(mat.pad[ind + 1, ind + 1]),
              S  = as.vector(mat.pad[ind + 1, ind    ]),
              SW = as.vector(mat.pad[ind + 1, ind - 1]),
              W  = as.vector(mat.pad[ind    , ind - 1]),
              NW = as.vector(mat.pad[ind - 1, ind - 1]))