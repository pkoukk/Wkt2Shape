# Wkt2Shape
Convert csv with wkt field to esri featureclass  
Support shapefile and filegdb(recommend)  
## Usage
Example:  
`X:\Python27\ArcGIS10.2\python.exe wkt2shape.py -w x:\file.gdb -f x:\target.csv -s geometryColumn -t POLYGON -n targetFeatureClass`

Arguments:  
-w, --workspace,  "path to save geometry"  
-f, --file,       "csv file to read"  
-s, --shape,      "wkt field to convert to geometry"  
-t, --type,       "geometry type. default:POINT,Support:POINT;MULTIPATCH;MULTIPOINT;POLYGON;POLYLINE"  
-n, --name,       "wkt field to convert to geometry"  
