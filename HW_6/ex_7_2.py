import arcpy
from arcpy import env
env.workspace = "U:\Shared\GIS\StuData\sescot3127\Python\Python_Exercises\Data\Exercise07"
fc = "roads.shp"
arcpy.AddField_management(fc, "FERRY", "TEXT", "", "", 20)
cursor = arcpy.da.UpdateCursor(fc, ["FEATURE", "FERRY"])
for row in cursor:
if row[0] == "Ferry Crossing":
row[1] = "YES"
else:
row[1]= "NO"
cursor.updateRow(row)






