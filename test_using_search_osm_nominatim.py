from pprint import pprint
import overpass
import urllib.parse
import requests
from bs4 import BeautifulSoup

# inspired by https://gist.github.com/4gus71n/26589a508d8deca333bb05928fd4beb0

def get_osm_relation_id(address):
    url = "https://www.openstreetmap.org/geocoder/search_osm_nominatim?query=" + \
        urllib.parse.quote(address)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    osm_link = soup.find('a', attrs={'class': 'set_position'})
    relation_id = osm_link.get('data-id').strip()
    # 3600000000 is the id offset
    return int(relation_id) + 3600000000


def load_street_names(address):
    id = get_osm_relation_id(address)
    street_names = []
    try:
        api = overpass.API()
        data = api.get(
            'area('+str(id)+')->.a; (way(area.a)["name"]["highway"]["highway" !~ "path"]["highway" !~ "steps"]["highway" !~ "motorway"]["highway" !~ "motorway_link"]["highway" !~ "raceway"]["highway" !~ "bridleway"]["highway" !~ "proposed"]["highway" !~ "construction"]["highway" !~ "elevator"]["highway" !~ "bus_guideway"]["highway" !~ "footway"]["highway" !~ "cycleway"]["foot" !~ "no"]["access" !~ "private"]["access" !~ "no"];node(w)(area.a););out;'
        )
        for f in data.features:
            if f.geometry['type'] == "LineString":
                street_names.append(f.properties['name'])
        # Remove duplicates
        street_names = list(dict.fromkeys(street_names))
        # Sort it
        street_names = sorted(street_names)
    except Exception as e:
        pprint(e)
    finally:
        return street_names


def nom_test(address):
    pass
    # id = get_osm_relation_id(address)
    # return id


def main():
    street_names = load_street_names("Notre, Brazil")
    pprint(street_names)
    # print(test("Mar del Plata, Buenos Aires, Argentina"))


main()
