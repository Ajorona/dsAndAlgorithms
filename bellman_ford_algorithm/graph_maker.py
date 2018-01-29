class Graph():
    def __init__(self, file_name):
        graph = Graph.get_graph(file_name)
        self.total_edges = graph["total_edges"]
        self.total_vertices = graph["total_vertices"]
        self.edge_list = graph["graph"]["edge_list"]
        self.vertex_list = graph["graph"]["vertex_list"]
        self.adjacency_list = graph["graph"]["adjacency_list"]
        self.distance_matrix = graph["distance_matrix"]

    class Adjacency():
        def __init__(self, vertex, weight):
            self.vertex = vertex
            self.weight = weight

    class Edge():
        def __init__(self, row):
            self.u = row[0]
            self.v = row[1]
            self.weight = row[2]

    @classmethod
    def get_graph(cls, file_name):
        with open(file_name, "rt") as graph_file:
            total_vertices, total_edges = [int(x) for x in graph_file.readline().split()]
            dist = [[float("Inf") for i in range(total_vertices + 1)] for j in range(total_vertices + 1)]
            raw_graph = cls.graph_maker(graph_file)
            dist = Graph.construct_distance_matrix(raw_graph, total_vertices, dist)
        return {"total_vertices" : total_vertices,
                "total_edges" : total_edges,
                "distance_matrix" : dist,
                "graph" : raw_graph
               }

    @classmethod
    def graph_maker(cls, graph_file):
        graph = {"edge_list" : [], "vertex_list" : [], "adjacency_list" : {}}
        for line in graph_file:
            edge = cls.Edge([int(x) for x in line.split()])
            graph["edge_list"].append(edge)

            if edge.u not in graph["adjacency_list"]:
                graph["adjacency_list"][edge.u] = [cls.Adjacency(edge.v, edge.weight)]
                graph["vertex_list"].append(edge.u)
            else:
                graph["adjacency_list"][edge.u].append([cls.Adjacency(edge.v, edge.weight)])
        return graph

    @classmethod
    def construct_distance_matrix(cls, raw_graph, total_vertices, distance_matrix):
        for edge in raw_graph["edge_list"]:
            if edge.weight < distance_matrix[edge.u][edge.v]:
                distance_matrix[edge.u][edge.v] = edge.weight
        for i in xrange(0, total_vertices):
            distance_matrix[i][i] = 0
        return distance_matrix
