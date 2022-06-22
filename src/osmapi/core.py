from xml.dom.minidom import Element
from requests import Response
from shapely.geometry import Polygon, LineString, MultiLineString
from shapely import ops
import osmapi.api as api
import osmapi.parser as parser
import pandas as pd
import geopandas


def get_latlng(element: Element) -> tuple:
    return float(element.getAttribute('lat')), float(element.getAttribute('lon'))


def get_node_latlng(root, id: str) -> tuple:
    for element in root.getElementsByTagName('node'):
        if element.getAttribute('id') == id:
            return get_latlng(element)


def get_way_points(root, wayID: str) -> list:
    points = []
    for element in root.getElementsByTagName('way'):
        if element.getAttribute('id') == wayID:
            for child in element.childNodes:
                if child.nodeName == 'nd':
                    points.append(get_node_latlng(
                        root, child.getAttribute('ref')))
    return points


def get_boundary(root) -> LineString:
    lines = []
    for node in root.getElementsByTagName('relation')[0].childNodes:
        if node.nodeName == 'member':
            if node.getAttribute('type') == 'way':
                way_reference = node.getAttribute('ref')
                points = get_way_points(root, way_reference)
                lines.append(LineString([[p[1], p[0]] for p in points]))
                multi_line = MultiLineString(lines)
    return ops.linemerge(multi_line)


def get_root(osm_id, type):
    response = api.get_object(type=type, osm_id=osm_id)
    root = parser.parse_response(response)
    return root


def get_relation_as_polygon(osm_id: str) -> Polygon:
    root = get_root(osm_id, 'relation')
    return Polygon(get_boundary(root))


def get_relation_as_gdf(osm_id: str) -> geopandas.GeoDataFrame:
    polygon = get_relation_as_polygon(osm_id)
    data = {'geometry': [polygon]}
    df = pd.DataFrame(data)
    gdf = geopandas.GeoDataFrame(df)
    return gdf


def get_way_as_line_string(osm_id: str) -> LineString:
    root = get_root(osm_id, 'way')
    points = get_way_points(root, osm_id)
    return LineString([[p[1], p[0]] for p in points])


def get_node_as_latlng(osm_id: str) -> tuple:
    root = get_root(osm_id, 'node')
    point = get_node_latlng(root, osm_id)
    return point
