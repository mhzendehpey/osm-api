import pytest
from osm_api.api import get_url, get_object


class OsmObject():

    _type = str
    _id = str

    def __init__(self, osm_type: str, osm_id: str):
        self._type = osm_type
        self._id = osm_id


relation = OsmObject('relation', '537701')
way = OsmObject('way', '440576851')
node = OsmObject('node', '25960293')


class TestGetUrl():

    def test_get_url_relation(self):
        assert get_url(
            relation._type, relation._id) == 'https://www.openstreetmap.org/api/0.6/relation/537701/full/'

    def test_get_url_way(self):
        assert get_url(
            way._type, way._id) == 'https://www.openstreetmap.org/api/0.6/way/440576851/full/'

    def test_get_url_node(self):
        assert get_url(
            node._type, node._id) == 'https://www.openstreetmap.org/api/0.6/node/25960293/'


class TestGetObject:

    def test_get_object_invalid_id(self):
        with pytest.raises(Exception):
            get_object(relation._type, way._id)

    def test_get_object_valid_id(self):
        assert get_object(relation._type, relation._id).status_code == 200
        assert get_object(way._type, way._id).status_code == 200
        assert get_object(node._type, node._id).status_code == 200
