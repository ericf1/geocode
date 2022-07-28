import osmium
import sqlite3
import pandas as pd
import time
# from data import DATA


class NodesHandler(osmium.SimpleHandler):
    def __init__(self):
        osmium.SimpleHandler.__init__(self)
        self.now_nodes_data = []
        self.nodes_counter = 0

    def node(self, n):
        if n.tags.get("addr:housenumber") and n.tags.get("addr:street"):
            lonlat = str(n.location).split('/')
            self.now_nodes_data.append({"id": n.id, "housenumber": n.tags.get("addr:housenumber"), "street": n.tags.get(
                "addr:street"), "lon": lonlat[0], "lat": lonlat[1]})
            print(f"Done with {self.nodes_counter}")
            self.nodes_counter = self.nodes_counter + 1


def main(osmfile):
    node_handler = NodesHandler()
    node_handler.apply_file(osmfile)
    return node_handler.now_nodes_data


if __name__ == '__main__':
    start = time.perf_counter()
    osm_file_loc = "C:\\Users\human\Desktop\\git\\geocode\\norte-latest.osm.pbf"
    con = sqlite3.connect('nodes.db')
    data = main(osm_file_loc)
    df = pd.DataFrame(data=data)
    df.to_sql(name="nodesdf", con=con, if_exists="replace")

    # test_handler = TestHandler()
    # test_handler.apply_file(osm_file_loc)

    finish = time.perf_counter()
    print(f'finished in {round((finish-start)/60, 2)} minutes(s)')
