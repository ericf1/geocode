import osmium
import generate_nodes
import sqlite3
import concurrent.futures


class WaysHandler(osmium.SimpleHandler):
    def node(self, n):
        if n.tags.get("addr:housenumber") and n.tags.get("addr:street"):
            try:
                lonlat = str(n.location).split('/')
                lon = lonlat[0]
                lat = lonlat[1]
                generate_nodes.insert_table(n.tags.get(
                    "addr:housenumber"), n.tags.get("addr:street"), lon, lat)
            except sqlite3.IntegrityError:
                print(dict(n.tags))

                # print(generate_nodes.read_table())
                # print(
                #     f'{n.tags.get("addr:housenumber")} {n.tags.get("addr:street")} {long} {lat}')

    # def way(self, w):
    #     if w.tags.get("highway") and w.tags.get("name"):
    #         for n in w.nodes:
    #             print(n.__dict__)


def main(osmfile):
    WaysHandler().apply_file(osmfile)


if __name__ == '__main__':
    osm_file_loc = "C:\\Users\human\Desktop\\git\\geocode\\norte-latest.osm.pbf"
    main(osm_file_loc)
