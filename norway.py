import folium
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os
from GPSPhoto import gpsphoto

image_dir = '/home/os/norway22/'

image_list = os.listdir(image_dir)
image_list = [x for x in image_list if x.endswith('jpg')]


for img in image_list:
    data = gpsphoto.getGPSData(image_dir + img)
    print(data)

m =  folium.Map(location=[61.6, 8.4])
m.save("norway.html")
