from xml.dom import minidom
from requests.models import Response


def parse_response(http_response: Response) -> minidom.Element:
    return minidom.parseString(http_response.content).childNodes[0]
