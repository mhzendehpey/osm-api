# OSMAPI Package
A small package to get data from OSM API directly

# Description
This package get Node, Way, and Relation geometry data directly from OSM API by provided OSM object ID.
Geometry data based on Shapely objects. due to heavy dependencies of GeoPandas, GeoDataFrame export excluded. but you can easily convert Shapely to GeoPandas, here is an example:

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