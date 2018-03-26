# Spatial File Metadata Collector Class
A Python Class to collect simple Metadata on several GIS file types using Fiona and Shapely.

I originally wrote this class for a former employer using GDAL Python bindings. I am now releasing
it to the world using the fantastic Shapely and Fiona libraries instead :).

## How to use
Simply copy the class into your script or copy SpatialMetadata.py into your project folder and 
import with:
'''python
import SpatialMetadata
'''

You can then specify a location to a layer and create a Spatialfile object:
'''python
my_layer = Spatialfile("/path/to/layer.shp")
'''

Once this is done, you can begin to get information on your layer by using syntax found in the
*Class methods* section of the readme. As an example however, to get the number of features
within the layer, you could simply use:
'''python
my_layer.get_feature_count()
14
'''

##
