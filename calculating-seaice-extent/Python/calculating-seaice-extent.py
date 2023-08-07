import urllib.request
import geopandas as gpd
from pyproj import CRS
import numpy as np


data_url = "https://polarwatch.noaa.gov/erddap/griddap/nsidcG02202v4nhmday.nc?cdr_seaice_conc_monthly[(2022-12-01T00:00:00Z):1:(2022-12-01T00:00:00Z)][(4851137.11):1:(-4850758.92)][(-3850000.0):1:(3750000.0)]"
urllib.request.urlretrieve(data_url, "seaice.nc")

ds = xr.open_dataset('seaice.nc')

#convert the xrray dataset to dataframe()
df = ds.to_dataframe()



# Assuming the projection is already Polar Stereographic,
# if not, you'll need to set it or convert it:
# gdf = gdf.to_crs('EPSG:xxxx') where xxxx is the EPSG code for your specific Polar Stereographic projection.

# Calculate area for each grid cell
gdf['area'] = gdf['geometry'].area / 10**6  # the area is in square meters, so divide by 10^6 to convert to square kilometers.

print(gdf['area'])


