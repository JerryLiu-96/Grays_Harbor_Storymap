import geojson

import json
class process_json():
    def __init__(self,year):
        self.year=year
    def process(self):
        url='assets/'+str(self.year)+'_coastline.geojson'
        print(url)
        f=open(url)
        data = json.load(f)
        li=[]
        for i in data["features"]:
            if i["properties"]["CLASS"]=="SHORELINE":
                li.append(i)
            
        tmp_name=str(self.year)+"_coastline"
        f_data={"type": "FeatureCollection",
                "name": tmp_name,
                "features": li}

        write_url='assets/f_'+str(self.year)+'_coastline.geojson'
        print(write_url)
        with open(write_url, 'w') as fp:
            geojson.dump(f_data, fp)

listed_year=[1911,1926,1941,1954]

for y in listed_year:
    
    process_json(y).process()