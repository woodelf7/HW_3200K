import arcpy
from arcpy import env
env.workspace = "U:\Shared\GIS\StuData\sescot3127\Python\Python_Exercises\Data\Exercise07\Results"
fc = r"U:\Shared\GIS\StuData\sescot3127\Python\Python_Exercises\Data\Exercise07\Results\airports.shp"
cursor = arcpy.da.SearchCursor(fc, "", '"FEATURE" = Airport')
arcpy.Buffer_analysis(cursor, r"U:\Shared\GIS\StuData\sescot3127\Python\Python_Exercises\Data\Exercise07\Results\buffer_air.shp", "15000 METERS")


import arcpy
from arcpy import env
env.workspace = "U:\Shared\GIS\StuData\sescot3127\Python\Python_Exercises\Data\Exercise07\Results"
fc = r"U:\Shared\GIS\StuData\sescot3127\Python\Python_Exercises\Data\Exercise07\Results\airports.shp"
cursor2 = arcpy.da.SearchCursor(fc, "", '"FEATURE" = Seaplane Base')
arcpy.Buffer_analysis(cursor2, r"U:\Shared\GIS\StuData\sescot3127\Python\Python_Exercises\Data\Exercise07\Results\buffer_sea.shp", "15000 METERS")

