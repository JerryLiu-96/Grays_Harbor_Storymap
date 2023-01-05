import json
import shapely
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
elev_array=gdal.Open(r'/Users/ziyangliu/Downloads/WA_SEW_dems/WA_SEW1_GCS_5m_NAVD88m.tif')
width=elev_array.RasterXSize        
height=elev_array.RasterYSize
ulx, xres, xskew, uly, yskew, yres = elev_array.GetGeoTransform()
print(width,height)
print(uly+yres*height)
#boundary of the clipped def file
c_ulx, c_uly=-124.1610,46.9198
c_lrx, c_lry= -124.0611,uly+yres*height
# path to where you want the clipped raster
outputSrtm = "/Users/ziyangliu/Downloads/WA_SEW_dems/clip_WA_SEW1_GCS_5m_NAVD88m.tif"
gdal.Translate(outputSrtm , elev_array, 
                    projWin = (c_ulx, c_uly,
                               c_lrx, c_lry)) # OR [ulx, uly, lrx, lry]

c_elev_array=gdal.Open(r'/Users/ziyangliu/Downloads/WA_SEW_dems/clip_WA_SEW1_GCS_5m_NAVD88m.tif')

c_width=c_elev_array.RasterXSize        
c_height=c_elev_array.RasterYSize
c_ulx, c_xres, c_xskew, c_uly, c_yskew, c_yres = c_elev_array.GetGeoTransform()
print("before clip ",width,height,ulx, xres, xskew, uly, yskew, yres)
print("after clip ",c_width,c_height,c_ulx, c_xres, c_xskew, c_uly, c_yskew, c_yres)

band1 = c_elev_array.GetRasterBand(1).ReadAsArray()

def getCoordinate(i,j):
    lon=c_ulx+c_xres*(j+1)
    lat=c_uly+c_yres*(i+1)
    return [lon,lat]

def elev_slr (x):
    mt = x*0.3048    #get the amount of sea level rise in unit of meter from feet
    band_mt = band1 - mt
    return band_mt

#define a function, to determine the case of the rectangle. 15 cases in total (see wikipedia "marching squares" for reference)
#a is the top left, b is the top right, c is the bottom right, d is the bottom left, in the clockwise sequence
#a, b, c, d are not the index, they're values of the referred point
def case(a,b,c,d):
    if a>0:
        if b>0:
            if c>0:
                if d>0:
                    case_num="0"
                else:
                    case_num="1"
            else:
                if d>0:
                    case_num="2"
                else:
                    case_num="3"
        else:
            if c>0:
                if d>0:
                    case_num="4"
                else:
                    case_num="5"
            else:
                if d>0:
                    case_num="6"
                else:
                    case_num="7"
    else:
        if b>0:
            if c>0:
                if d>0:
                    case_num="8"
                else:
                    case_num="9"
            else:
                if d>0:
                    case_num="10"
                else:
                    case_num="11"
        else:
            if c>0:
                if d>0:
                    case_num="12"
                else:
                    case_num="13"
            else:
                if d>0:
                    case_num="14"
                else:
                    case_num="15"
    return case_num

line_list=[]
for y in np.arange(len(band1[0])-1):
    print(y)
    for x in np.arange(145,2047):
        matrix_slr=elev_slr(1)
        top_left_elev = matrix_slr[x][y]
        top_right_elev = matrix_slr[x][y+1]
        bottom_left_elev = matrix_slr[x+1][y]
        bottom_right_elev = matrix_slr[x+1][y+1]
        caseNum=case(top_left_elev,top_right_elev,bottom_right_elev,bottom_left_elev)
        if caseNum=="0" or caseNum=="15":
                continue
        #if it is case 5 or 10, then we need to get the value of the saddle point
        elif caseNum=="5":
            #get the value of the center point
            avg_elev=0.25 * (top_left_elev + top_right_elev + bottom_left_elev + bottom_right_elev)
            mid_x_axis = getCoordinate(x,y)[0]
            mid_y_axis= getCoordinate(x,y)[1]
            if avg_elev>0:
                    
                line1=[[mid_x_axis,mid_y_axis-0.5*yres],[mid_x_axis+0.5*xres,mid_y_axis]]
                line2=[[mid_x_axis-0.5*xres,mid_y_axis],[mid_x_axis,mid_y_axis+0.5*yres]]
                line_list.append(line1)
                line_list.append(line2)
            else:
                    line1=[[mid_x_axis-0.5*xres,mid_y_axis],[mid_x_axis,mid_y_axis-0.5*yres]]
                    line2=[[mid_x_axis,mid_y_axis+0.5*yres],[mid_x_axis+0.5*xres,mid_y_axis]]
                    line_list.append(line1)
                    line_list.append(line2)
        elif caseNum=="10":
            avg_elev=0.25 * (top_left_elev + top_right_elev + bottom_left_elev + bottom_right_elev)
            mid_x_axis = getCoordinate(x,y)[0]
            mid_y_axis= getCoordinate(x,y)[1]
            if avg_elev>0:
                line1=[[mid_x_axis-0.5*xres,mid_y_axis],[mid_x_axis,mid_y_axis-0.5*yres]]
                line2=[[mid_x_axis,mid_y_axis+0.5*yres],[mid_x_axis+0.5*xres,mid_y_axis]]
                line_list.append(line1)
                line_list.append(line2)
            else:
                line1=[[mid_x_axis,mid_y_axis-0.5*yres],[mid_x_axis+0.5*xres,mid_y_axis]]
                line2=[[mid_x_axis-0.5*xres,mid_y_axis],[mid_x_axis,mid_y_axis+0.5*yres]]
                line_list.append(line1)
                line_list.append(line2)
        elif caseNum=="1" or caseNum=="14":
            mid_x_axis = getCoordinate(x,y)[0]
            mid_y_axis= getCoordinate(x,y)[1]
            line1=[[mid_x_axis-0.5*xres,mid_y_axis],[mid_x_axis,mid_y_axis+0.5*yres]]
            line_list.append(line1)
        elif caseNum=="2" or caseNum=="13":
            mid_x_axis = getCoordinate(x,y)[0]
            mid_y_axis= getCoordinate(x,y)[1]
            line1=[[mid_x_axis,mid_y_axis+0.5*yres],[mid_x_axis+0.5*xres,mid_y_axis]]
            line_list.append(line1)
        elif caseNum=="3":
            mid_x_axis = getCoordinate(x,y)[0]
            mid_y_axis= getCoordinate(x,y)[1]
            line1=[[mid_x_axis-0.5*xres,mid_y_axis],[mid_x_axis+0.5*xres,mid_y_axis]]
            line_list.append(line1)
        elif caseNum=="4" or caseNum=="11":
            mid_x_axis = getCoordinate(x,y)[0]
            mid_y_axis= getCoordinate(x,y)[1]
            line1=[[mid_x_axis,mid_y_axis-0.5*yres],[mid_x_axis+0.5*xres,mid_y_axis]]
            line_list.append(line1)
        elif caseNum=="6":
            mid_x_axis = getCoordinate(x,y)[0]
            mid_y_axis= getCoordinate(x,y)[1]
            line1=[[mid_x_axis,mid_y_axis-0.5*yres],[mid_x_axis,mid_y_axis+0.5*yres]]
            line_list.append(line1)
        elif caseNum=="7" or caseNum=="8":
            mid_x_axis = getCoordinate(x,y)[0]
            mid_y_axis= getCoordinate(x,y)[1]
            line1=[[mid_x_axis-0.5*xres,mid_y_axis],[mid_x_axis,mid_y_axis-0.5*yres]]
            line_list.append(line1)
        elif caseNum=="9":
            mid_x_axis = getCoordinate(x,y)[0]
            mid_y_axis= getCoordinate(x,y)[1]
            line1=[[mid_x_axis,mid_y_axis-0.5*yres],[mid_x_axis,mid_y_axis+0.5*yres]]
            line_list.append(line1)
        elif caseNum=="12":
            mid_x_axis = getCoordinate(x,y)[0]
            mid_y_axis= getCoordinate(x,y)[1]
            line1=[[mid_x_axis-0.5*xres,mid_y_axis],[mid_x_axis+0.5*xres,mid_y_axis]]
            line_list.append(line1)

line_json=[]
all_line_segments=line_list
print("number of line segment is ",len(all_line_segments))
while len(all_line_segments)>0:
    print(len(line_json),len(all_line_segments))
    #create a list named line_string to store each line
    line_string=[]
    first_pt=all_line_segments[0][0]
    second_pt=all_line_segments[0][1]
    line_string.append(first_pt)
    line_string.append(second_pt)
    all_line_segments.remove(all_line_segments[0])

    
    while any(second_pt in sl for sl in all_line_segments):
        for i in range(len(all_line_segments)):
            for j in range(2):
                if all_line_segments[i][j]==second_pt:
                    if j==0:

                        line_string.append(all_line_segments[i][1])
                        second_pt=all_line_segments[i][1]
                        all_line_segments.remove(all_line_segments[i])
                    else:
                        line_string.append(all_line_segments[i][0])
                        second_pt=all_line_segments[i][0]
                        all_line_segments.remove(all_line_segments[i])
                    break
            else:
                continue    
            break
    while any(first_pt in sl for sl in all_line_segments):
        for i in range(len(all_line_segments)):
            for j in range(2):
                if all_line_segments[i][j]==first_pt:
                    if j==0:
                        line_string=[all_line_segments[i][1]]+line_string
                        first_pt=all_line_segments[i][1]
                        all_line_segments.remove(all_line_segments[i])
                    else:
                        line_string=[all_line_segments[i][0]]+line_string
                        first_pt=all_line_segments[i][0]
                        all_line_segments.remove(all_line_segments[i])
                    break
            else:
                continue
            break
    
    #if the line string is a basin, then we should not append it to the final list
    if line_string[0]==line_string[-1]:
        poly=Polygon([tuple(i) for i in line_string])
        if (line_string[0][0]-ulx)%xres==0:
            pt=Point(line_string[0][0]+0.5*xres,line_string[0][1])
            pt_value=elev_slr(1)[(c_uly-line_string[0][1])//abs(yres)][(line_string[0][0]-c_ulx)//xres]
            if poly.contains(pt):
                if pt_value>0:
                    line_json.append(line_string)
            else:
                if pt_value<=0:
                    line_json.append(line_string)
        else:
            pt=Point(line_string[0][0],line_string[0][1]+0.5*yres)
            pt_value=elev_slr(1)[(c_uly-line_string[0][1])//abs(yres)][(line_string[0][0]-c_ulx)//xres]
            if poly.contains(pt):
                if pt_value>0:
                    line_json.append(line_string)
            else:
                if pt_value<=0:
                    line_json.append(line_string)
        
    else:
        line_json.append(line_string)


print(line_json)
    

data={
    "type": "FeatureCollection",
    "features": [ 
        {
            "type": "Feature", 
            "geometry":{
        "type": "MultiLineString",
        "coordinates": line_json
    }}]
   }

with open('/Users/ziyangliu/Downloads/WA_SEW_dems/data_1ft.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)    