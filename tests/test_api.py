import pytest
from osm_api.api import get_url, get_object


class TestGetUrl():

    def test_get_url_relation(self):
        assert get_url(
            'relation', '537701') == 'https://www.openstreetmap.org/api/0.6/relation/537701/full/'

    def test_get_url_way(self):
        assert get_url(
            'way', '440576851') == 'https://www.openstreetmap.org/api/0.6/way/440576851/full/'

    def test_get_url_node(self):
        assert get_url(
            'node', '25960293') == 'https://www.openstreetmap.org/api/0.6/node/25960293/'


class TestGetObject:

    def test_get_object(self):
        with pytest.raises(Exception):
            get_object('relation', '584565')
