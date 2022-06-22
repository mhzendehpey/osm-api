# OSMAPI Package
A small package to get data from [OpenStreetMap API](https://www.openstreetmap.org/) directly

# Description
This package get Node, Way, and Relation geometry data directly from OSM API(instead of [Nominatim API](https://nominatim.openstreetmap.org/ui/details.html)) by provided OSM object ID, and parse it into [Shapely](https://pypi.org/project/Shapely/) objects. due to heavy dependencies of [GeoPandas](https://geopandas.org/en/stable/getting_started/install.html#dependencies), GeoDataFrame export excluded. but you can easily convert Shapely to GeoPandas, here is an example:

```python
def get_relation_as_gdf(osm_id: str) -> geopandas.GeoDataFrame:
    polygon = get_relation_as_polygon(osm_id)
    data = {'geometry': [polygon]}
    df = pd.DataFrame(data)
    gdf = geopandas.GeoDataFrame(df)
    return gdf
```

# Examples

```python
import osmapi
polygon = osmapi.get_relation(osm_id='537701')
line_string = osmapi.get_way(osm_id='440582504')
lat_lng = osmapi.get_node(osm_id='25960293')
```