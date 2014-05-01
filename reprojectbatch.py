##[Example scripts]=group
##input=folder
##output=folder
targetcrs = 'EPSG:4326'
import os
from PyQt4.QtCore import QFileInfo,QSettings
from qgis.core import QgsRasterLayer

vectorsprocess = []
rastersprocess = []
for theinput in os.listdir(input):
    try:
        if theinput.split(".")[1] == "shp":
            vectorsprocess.append(theinput)
        elif theinput.split(".")[1] in ["tif", "tiff","geotiff"]:
            rastersprocess.append(theinput)
    except:
       continue
print vectorsprocess
print rastersprocess

for thevector in vectorsprocess:
    inputname = thevector.split("/")[-1]
    outputfile = output + "/" + inputname
    processing.runalg("qgis:reprojectlayer",input + "/" + thevector,targetcrs,outputfile)

for theraster in rastersprocess:
    inputname = theraster.split("/")[-1]
    outputfile = output + "/" + inputname
   
    fileInfo = QFileInfo(input + "/" + theraster)
    baseName = fileInfo.baseName()
    rlayer = QgsRasterLayer(input + "/" + theraster, baseName)
    srcproj = "EPSG:4326"
    if rlayer.crs().authid() != "":
        srcproj = rlayer.crs().authid()
    print srcproj
    processing.runalg("gdalogr:warpreproject",input + "/" + theraster,srcproj,targetcrs,0,0,"",outputfile)
  