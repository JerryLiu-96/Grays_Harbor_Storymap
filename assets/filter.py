import geojson

import json
# Opening JSON file
f = open('assets/2006_coastline.geojson')
 
# returns JSON object as
# a dictionary
data = json.load(f)

# create a new list to store the filtered dictionaries
li=[]

#only keep the dictionaries which contain the natural mean high water in the attribute
for i in data["features"]:
    if i["properties"]["CLASS"]=="SHORELINE":
        li.append(i)
print(li)

f_data={"type": "FeatureCollection",
"name": "2006_coastline",
"features": li}

with open('assets/f_2006_coastline.geojson', 'w') as fp:
    geojson.dump(f_data, fp)
