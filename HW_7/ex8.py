import arcpy
from arcpy import env
env.workspace = "U:\Shared\GIS\StuData\sescot3127\Python\Python_Exercises\Data\Exercise08"
fc = "newpoly2.shp"
arcpy.CreateFeatureclass_management("C:/Data", fc, "Polygon")
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])
array = arcpy.Array()
coordlist =[[0, 0], [0, 1000], [1000, 1000], [1000, 0]]
for x, y in coordlist:
point = arcpy.Point(x,y)
array.append(point)
polygon = arcpy.Polygon(array)
cursor.insertRow([polygon])
del cursor

import arcpy
from arcpy import env
env.workspace = "U:\Shared\GIS\StuData\sescot3127\Python\Python_Exercises\Data\Exercise08"
fc = "Hawaii.shp"
newfc = "Results/Hawaii_single.shp"
arcpy.MultipartToSinglepart_management(fc, newfc)
spatialref = arcpy.Describe(newfc).spatialReference
unit = spatialref.linearUnitName
cursor = arcpy.da.SearchCursor(newfc, ["SHAPE@"])
for row in cursor:
print ("{0} square {1}".format(row[0].area, unit))


import arcpy
from arcpy import env
env.workspace = "U:\Shared\GIS\StuData\sescot3127\Python\Python_Exercises\Data\Exercise08 "
fc = "Hawaii.shp"
newfc = "envelope8.shp"
desc = arcpy.Describe(fc)
spatialref = desc.spatialReference
extent = desc.extent
arcpy.CreateFeatureclass_management("U:\Shared\GIS\StuData\sescot3127\Python\Python_Exercises\DataExercise08", newfc, "Polygon", "", "", "", spatialref)
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
array.append(extent.upperLeft)
array.append(extent.upperRight)
array.append(extent.lowerRight)
array.append(extent.lowerLeft)
polygon = arcpy.Polygon(array)
cursor.insertRow([polygon])
del cursor
Exercise 9
Challenge 1
