## Mapping data on Polarstereographic projected map
>NOAA CoastWatch/PolarWatch
>
>history | Created Mar 2023

**Content**

-  python notebook file: mapping-with-different-projections.ipynb
-  data file : data/PB_Argos.csv


**The exercise demonstrates the following techniques:**

-  Accessing satellite data from ERDDAP
-  Making a projected map
-  Adding projected data
-  Adding geographical data

**Datasets used:**

- sea ice data:  (stereographic projection) will be downloaded in netCDF format from <a href="https://polarwatch.noaa.gov/data-server/erddapinfo.html" target="_blank">PolarWatch ERDDAP server</a>
- polar bear tracking data :  (geographical reference) will be downloaded in csv format from <a href="https://borealisdata.ca/file.xhtml?fileId=151017&version=1.0)" target="_blank">https://borealisdata.ca/file.xhtml?fileId=151017&version=1.0)</a> 

**Python Packaged used**

- netCDF4 (reading data and metadata from netCDF file)
- matplotlib (ploting maps)
- cartopy (projecting data, creating projected basemap)
- pandas (data analysis)
