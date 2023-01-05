from ftplib import all_errors
from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

# import DEM file of SEW 1, the bound of this DEM file is (-124.40898193837502 47.37482299379318) (-123.15708193837501 46.79004799379318)
elev_array=gdal.Open(r'/Users/ziyangliu/Downloads/WA_SEW_dems/WA_SEW1_GCS_5m_NAVD88m.tif')

#get the bound of this DEM file
width=elev_array.RasterXSize        
height=elev_array.RasterYSize
ulx, xres, xskew, uly, yskew, yres = elev_array.GetGeoTransform()

#print the bound of the dem file, -124.40898193837502 47.37482299379318 -123.15708193837501 46.79004799379318
print(ulx, uly, ulx+width*xres, uly+height*yres)
print("yres is ", yres,"  x res is ", xres, "width is ", width, "height is ", height, "num of pixels is ", width*height)

#extract the elevation values from the file, and read as Array
band1 = elev_array.GetRasterBand(1).ReadAsArray()

print("The heighest point is ",np.max(band1))

#define a function, get the elevation with sea level rise applied
#the x is given in feet
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




            
#apply marching square algorithm to get the shoreline, which is the contour line of elevation 0.
#ft determine the amount of sea level rise
def line(ft):
    #create an empty list to save the line sections
    line_list=[]
    matx_ft=elev_slr(ft)
    for i in np.arange(width-1):
        for j in np.arange(height-1):
            top_left_elev = matx_ft[j][i]
            top_right_elev = matx_ft[j][i+1]
            bottom_left_elev = matx_ft[j+1][i]
            bottom_right_elev = matx_ft[j+1][i+1]
            caseNum=case(top_left_elev,top_right_elev,bottom_right_elev,bottom_left_elev)

            # if it is case 0 or 15, then there is no line
            if caseNum=="0" or caseNum=="15":
                continue
            
            #if it is case 5 or 10, then we need to get the value of the saddle point
            elif caseNum=="5":
                #get the value of the center point
                avg_elev=0.25 * (top_left_elev + top_right_elev + bottom_left_elev + bottom_right_elev)
                mid_x_axis = ulx + xres*(i+1)
                mid_y_axis= uly + yres*(j+1)
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
                mid_x_axis = ulx + xres*(i+1)
                mid_y_axis= uly + yres*(j+1)
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
                mid_x_axis = ulx + xres*(i+1)
                mid_y_axis= uly + yres*(j+1)
                line1=[[mid_x_axis-0.5*xres,mid_y_axis],[mid_x_axis,mid_y_axis+0.5*yres]]
                line_list.append(line1)
            elif caseNum=="2" or caseNum=="13":
                mid_x_axis = ulx + xres*(i+1)
                mid_y_axis= uly + yres*(j+1)
                line1=[[mid_x_axis,mid_y_axis+0.5*yres],[mid_x_axis+0.5*xres,mid_y_axis]]
                line_list.append(line1)
            elif caseNum=="3":
                mid_x_axis = ulx + xres*(i+1)
                mid_y_axis= uly + yres*(j+1)
                line1=[[mid_x_axis-0.5*xres,mid_y_axis],[mid_x_axis+0.5*xres,mid_y_axis]]
                line_list.append(line1)
            elif caseNum=="4" or caseNum=="11":
                mid_x_axis = ulx + xres*(i+1)
                mid_y_axis= uly + yres*(j+1)
                line1=[[mid_x_axis,mid_y_axis-0.5*yres],[mid_x_axis+0.5*xres,mid_y_axis]]
                line_list.append(line1)
            elif caseNum=="6":
                mid_x_axis = ulx + xres*(i+1)
                mid_y_axis= uly + yres*(j+1)
                line1=[[mid_x_axis,mid_y_axis-0.5*yres],[mid_x_axis,mid_y_axis+0.5*yres]]
                line_list.append(line1)
            elif caseNum=="7" or caseNum=="8":
                mid_x_axis = ulx + xres*(i+1)
                mid_y_axis= uly + yres*(j+1)
                line1=[[mid_x_axis-0.5*xres,mid_y_axis],[mid_x_axis,mid_y_axis-0.5*yres]]
                line_list.append(line1)
            elif caseNum=="9":
                mid_x_axis = ulx + xres*(i+1)
                mid_y_axis= uly + yres*(j+1)
                line1=[[mid_x_axis,mid_y_axis-0.5*yres],[mid_x_axis,mid_y_axis+0.5*yres]]
                line_list.append(line1)
            elif caseNum=="12":
                mid_x_axis = ulx + xres*(i+1)
                mid_y_axis= uly + yres*(j+1)
                line1=[[mid_x_axis-0.5*xres,mid_y_axis],[mid_x_axis+0.5*xres,mid_y_axis]]
                line_list.append(line1)
    return line_list



#function to sort these shoreline sections into shorelines
def assembly(ft):
    #create a list to store the final result
    line_json=[]
    all_line_segments=line(ft)
    print("number of line segment is ",len(all_line_segments))
    while len(all_line_segments)>0:
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
                pt_value=elev_slr(ft)[(uly-line_string[0][1])//abs(yres)][(line_string[0][0]-ulx)//xres]
                if poly.contains(pt):
                    if pt_value>0:
                        line_json.append(line_string)
                else:
                    if pt_value<=0:
                        line_json.append(line_string)
            else:
                pt=Point(line_string[0][0],line_string[0][1]+0.5*yres)
                pt_value=elev_slr(ft)[(uly-line_string[0][1])//abs(yres)][(line_string[0][0]-ulx)//xres]
                if poly.contains(pt):
                    if pt_value>0:
                        line_json.append(line_string)
                else:
                    if pt_value<=0:
                        line_json.append(line_string)
            
        else:
            line_json.append(line_string)
    
    return line_json

print(assembly(1))
                            
""" 
elif any(first_pt in sl for sl in all_line_segments):



        #create a variable to record how many times the 
        count=0
        while count<len(all_line_segments):
            
            for lineSects in all_line_segments:
                count=count+1
                
                if second_pt in lineSects:
                    count=0
                    if lineSects[0]==second_pt:
                        line_string.append(lineSects[1])
                        second_pt=lineSects[1]
                    else:
                        line_string.append(lineSects[0])
                        second_pt=lineSects[0]
                    all_line_segments.remove(lineSects)
                    break
    

"""
           