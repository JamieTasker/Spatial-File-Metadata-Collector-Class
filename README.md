# Spatial File Metadata Collector Class
**PLEASE NOTE - Readme not quite finished yet. Refer to comments in SpatialMetadata.py for more information.**

A Python Class to collect simple Metadata on several GIS file types using Fiona and Shapely.

I originally wrote this class for a former employer using GDAL Python bindings. I am now releasing
it to the world using the fantastic Shapely and Fiona libraries instead :).

## How to use
Simply copy the class into your script or copy SpatialMetadata.py into your project folder and 
import with:
```python
import SpatialMetadata
```

You can then specify a location to a layer and create a Spatialfile object:
```python
my_layer = Spatialfile("/path/to/layer.shp")
```

Once this is done, you can begin to get information on your layer by using syntax found in the
*Class methods* section of the readme. As an example however, to get the number of features
within the layer, you could simply use:
```python
my_layer.get_feature_count()
14
```

## Class methods
```python
# Return the file name of the layer
my_layer.get_layer_name()
layer.shp

# Return a date string consisting of when the layer was last modified.
# Please note that this method uses the date modified of the file path initially specified when 
# the object was created. This means that if you initially point to a .shp file, it will only 
# display the date modified of this file, not the associated .dbf, .prj or .shx files.
my_layer.get_date_modified()

