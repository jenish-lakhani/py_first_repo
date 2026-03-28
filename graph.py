class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dist = {}
        for start, end in self.edges:
            if start in self.graph_dist:
                self.graph_dist[start].append(end)
            else:
                self.graph_dist[start] = [end]
        print("graph_dist", self.graph_dist)

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dist:
            return []

        paths = []
        for node in self.graph_dist[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shorted_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dist:
            return None

        shortest_path = None
        for node in self.graph_dist[start]:
            sp = self.get_shorted_path(node, end, path)
            if sp:
                if shortest_path is None or len(sp) < len(shortest_path):
                    shortest_path = sp
        return shortest_path


if __name__ == "__main__":
    routes = [
        ("mumbai", "paris"),
        ("mumbai", "dubai"),
        ("paris", "dubai"),
        ("paris", "new york"),
        ("dubai", "new york"),
        ("new york", "toronto"),
    ]
    route_graph = Graph(routes)
    start = "mumbai"
    end = "new york"
    print(
        f"shortest paths between {start} and {end} :",
        route_graph.get_shorted_path(start, end),
    )
