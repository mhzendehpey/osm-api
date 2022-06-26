[![PyPI version](https://badge.fury.io/py/osmapi-wrapper.svg)](https://pypi.org/project/osmapi-wrapper/) 
[![codecov](https://codecov.io/gh/mhzendehpey/osm-api/branch/master/graph/badge.svg?token=TGNWNW54EI)](https://codecov.io/gh/mhzendehpey/osm-api)

# osm_api Package
A small package to get data from [OpenStreetMap](https://www.openstreetmap.org/) API directly

# Description
This package get Node, Way, and Relation geometry data directly from OSM API(instead of [Nominatim API](https://nominatim.openstreetmap.org/ui/details.html)) by provided OSM object ID, and parse it into [Shapely](https://pypi.org/project/Shapely/) objects. due to heavy dependencies of [GeoPandas](https://geopandas.org/en/stable/getting_started/install.html#dependencies), GeoDataFrame export excluded. but you can easily convert Shapely to GeoPandas, here is an example:

```python
def get_relation_as_gdf(osm_id: str) -> geopandas.GeoDataFrame:
    polygon = osm_api.get_relation(osm_id)
    data = {'geometry': [polygon]}
    gdf = geopandas.GeoDataFrame(data)
    return gdf
```

# Examples

```python
import osm_api
polygon = osm_api.get_relation(osm_id='537701')
line_string = osm_api.get_way(osm_id='440582504')
lat_lng = osm_api.get_node(osm_id='25960293')
```
