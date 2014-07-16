import arcpy
from arcpy import env
arcpy.env.workspace = "U:\Shared\GIS\StuData\sescot3127\Python\Python Exercises\Data\Exercise06"
fclist = arcpy.ListFeatureClasses()

for feature in fclist:
    myshape = arcpy.Describe(feature)
    print "{} is a {} {}".format(myshape.name, myshape.shapeType, myshape.datasetType)

arcpy.CreateFileGDB_management("U:/Shared/GIS/StuData/sescot3127/Python/Python Exercises/Data/Exercise06/Results", "NM.gdb")
for fc in fclist:
    shape =  arcpy.Describe(fc)
    if shape.shapeType == u'Polygon':
        arcpy.CopyFeatures_management(fc, "U:/Shared/GIS/StuData/sescot3127/Python/Python Exercises/Data/Exercise06/Results/NM.gbd/" + shape.basename)
        
