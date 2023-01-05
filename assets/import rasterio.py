print("Hellp!")
#import rasterio
from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
elev_array=gdal.Open(r'/Users/ziyangliu/Downloads/WA_SEW_dems/WA_SEW1_GCS_5m_NAVD88m.tif')
width=elev_array.RasterXSize
height=elev_array.RasterYSize
ulx, xres, xskew, uly, yskew, yres = elev_array.GetGeoTransform()
print(ulx,uly,ulx+width*xres,uly+height*yres)
band1 = elev_array.GetRasterBand(1).ReadAsArray()
print(band1)
print(np.max(band1))
band1_1ft=band1 - 0.3048
print(band1_1ft)

dems={}
for i in range(1,11):
    slr_meter=i*0.3048
    dems['slr_'+str(i)]=band1 - slr_meter
print(dems['slr_1'])
plt.figure()
plt.imshow(band1)
plt.colorbar()
plt.show()
print(band1[0][5])
coordinate_list=[]
shoreline_json={"type": "FeatureCollection","name": "DEM_coastline_bay","features":[{"type": "Feature","properties":{},"geometry":{"type":"MultiLineString","coordinates":[coordinate_list]}}]}