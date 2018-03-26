# Spatial Metadata Collector.py v1.0
# A class to collect metadata on flat spatial files.
# Created by Jamie Tasker on 18/01/2018.
# Last updated on 18/01/2017.

import os
import datetime
from shapely.geometry import shape
import osgeo
import fiona
from fiona.crs import to_string


class Spatialfile(object):

    # Initialize the file.
    def __init__(self, filepath):

        self.filepath = filepath
        try:
            # Use fiona to open the file.
            self.layer = fiona.open(self.filepath)
            # Create a list of shapely geometries that relate to each each feature within the layer.
            self.geometries = [shape(feature["geometry"]) for feature in self.layer]
        except Exception as e:
            # If file cannot be opened, a error message is printed and None is returned.
            raise SpatialFileException(self.filepath + " cannot be opened with Fiona's supported \
drivers.")

    def get_layer_name(self):
        """Get the layer filename"""

        # Simply split the filename from the extension and return it. 
        return os.path.split(self.filepath)[1]

    def get_date_modified(self):
        """Get the date the file was last modified."""

        # Return the date the file was modified as a string. We use strftime to convert from epoch.
        return datetime.datetime.fromtimestamp(os.path.getmtime(self.filepath)).strftime\
        ('%d/%m/%Y %H:%M:%S')

    def get_date_created(self):
        """Get the date the file was created"""

        # Same again, only this time we get the date the file was created.
        return datetime.datetime.fromtimestamp(os.path.getctime(self.filepath)).strftime\
        ('%d/%m/%Y %H:%M:%S')

    def get_layer_driver(self):
        """Get the driver fiona has used to open the file"""

        # Return the driver that has been used to open the layer. This will tell us what format the
        # file is in.
        return self.layer.driver

    def get_feature_count(self):
        """ Return the number of features within the layer."""

        return len(self.geometries)

    def get_feature_geom_types(self):
        """Return the number of individual points, lines and polygons"""

        polygons = 0
        lines = 0
        points = 0
        others = 0

        # The for loop runs through each geometry and checks what type they are. Shapely's 
        # "geom_type" attribute allows us to directly access whether the feature is a point, line
        # or polygon.
        for feature in self.geometries:
            if feature.geom_type == "Polygon":
                polygons += 1
            elif feature.geom_type == "Line":
                lines += 1
            elif feature.geom_type == "Point":
                points += 1
            else:
                others += 1

        return polygons, lines, points, others

    def invalid_geom_count(self):
        """Count the number of invalid geometries"""

        invalid_geom = 0
        # We loop through the geometries again, only this time we use is_valid to filter out
        # features that contain invalid geometries.
        for feature in self.geometries:
            if not feature.is_valid:
                invalid_geom += 1

        return invalid_geom

    def get_layer_projection(self):
        """Get the projection system of the layer"""

        # We use to_string to return the crs system as a string rather than a dictionary.
        return to_string(self.layer.crs)

    def get_layer_extent(self):
        """Get the extent of the layer"""

        # Returns a tuple containing bounding box information of the layer.
        return self.layer.bounds

    def get_field_names(self):
        """Get the name, type and length of each field"""

        # Extract the properties from the layer schema. The properties item tells us the each field
        # name, length and type.
        properties = dict((self.layer.schema["properties"]))

        # Use dictionary comprehension to return the fields in the following format:
        # "Field_Name": "Str: 54".
        return {k: v for k, v in properties.items()}

class SpatialFileException(Exception):
    pass
