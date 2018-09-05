import os
import arcpy
import csv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-w", "--workspace", required=True,help="path to save geometry")
ap.add_argument("-f", "--file", required=True,help="csv file to read")
ap.add_argument("-s", "--shape", required=True,help="wkt field to convert to geometry")
ap.add_argument("-t", "--type", type=str, default="POINT",help="geometry type default:POINT.Support:POINT;MULTIPATCH;MULTIPOINT;POLYGON;POLYLINE")
ap.add_argument("-n", "--name", type=str, default=None,help="wkt field to convert to geometry")
args=vars(ap.parse_args())

workspace=args['workspace']
file=args['file']
geometry_field=args['shape']
geometry_type=args['type']
class_name=args['name']
if (class_name is None):
    class_name=os.path.splitext(os.path.basename(file))[0]
if (not workspace.endswith('.gdb')):
    class_name=class_name+'.shp'

arcpy.env.workspace=workspace
print("--------start to read files--------")
if (not arcpy.Exists(class_name)):
    print("creating feature class %s" %class_name)
    arcpy.CreateFeatureclass_management(workspace,class_name,geometry_type)

def create_fields(fields):
    class_describe=arcpy.Describe(class_name)
    class_fields=map(lambda x:x.name,class_describe.fields)
    for field in fields:
        if(field not in class_fields):
            print("creating field %s" % field)
            arcpy.AddField_management(class_name,field,'TEXT')

with open(file,'rb') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    field_names=list()
    field_names.extend(csv_reader.fieldnames)
    create_fields(field_names)
    field_names.append('SHAPE@WKT')
    print("--------start to create features--------")
    cursor=arcpy.da.InsertCursor(class_name,field_names)
    for row in csv_reader:
        v=[row[f] for f in csv_reader.fieldnames]
        v.append(row[geometry_field])
        cursor.insertRow(tuple(v))
    del cursor
    print("--------all features are created--------")




