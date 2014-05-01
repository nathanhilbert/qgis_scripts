##[Example scripts]=group
##input=folder
##breakers=folder
##output=folder
import os
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

clipfiles = []
for breakerfile in os.listdir(breakers):
    try:
        if breakerfile.split(".")[1] == "shp":
            clipfiles.append(breakerfile)
    except:
       continue

for thevector in vectorsprocess:
    inputname = thevector.split(".")[0].split("/")[-1]
    for inputbreak in clipfiles:
        outputfile = output + "/" + inputname + "_" + inputbreak
        print outputfile
        processing.runalg("qgis:clip", input + '/' + thevector, breakers + '/' + inputbreak,outputfile)
        

for theraster in rastersprocess:
    inputname = theraster.split(".")[0].split("/")[-1]
    for inputbreak in clipfiles:
        outputfile = output + "/" + inputname + "_" + inputbreak.replace(".shp", ".tif")
        print input + '/' + theraster
        print breakers + '/' + inputbreak
        print outputfile
        processing.runalg("gdalogr:cliprasterbymasklayer", input + '/' + theraster, breakers + '/' + inputbreak,None,None,None,None,outputfile)

        