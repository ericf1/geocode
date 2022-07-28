class TestHandler(osmium.SimpleHandler):
    def __init__(self):
        osmium.SimpleHandler.__init__(self)
        self.relation_to_ways = []
        self.relation_counter = 0

    # def relation(self, r):
    #     # Admin_Level 8 is a municipality
    #     if "is_in:country" in r.tags and r.tags.get("is_in:country") != "Brazil":
    #         return
    #     if not ("wikipedia" in r.tags and "pt" in r.tags.get("wikipedia")):
    #         return
    #     if "admin_level" in r.tags and r.tags.get("admin_level") == "8":
    #         for w in r.members:
    #             self.relation_counter = self.relation_counter + 1
    #             w = str(w)
    #             if "w" in w:
    #                 # get rid of "@outer" and "w"
    #                 self.relation_to_ways.append(w[1:-6])

        # self.nodes_data[n.id] = {"id": n.id, "housenumber": n.tags.get("addr:housenumber"), "street": n.tags.get(
        #     "addr:street"), "lon": lonlat[0], "lat": lonlat[1]}

    def way(self, w):
        for n in w.nodes:
            print(str(n))
        # print(w.nodes)
        # if not str(w.id) in self.relation_to_ways:
        #     return
        # print(w)
