
from graph_maker import Graph

class Run_Floyd_Warshall_Algorithm():
    def __init__(self, graph):
        dist = graph.distance_matrix
        for k in range(graph.total_vertices):
            for u in range(graph.total_vertices):
                for v in range(graph.total_vertices):
                    if dist[u][v] > dist[u][k] + dist[k][v]:
                        dist[u][v] = dist[u][k] + dist[k][v]
        self.dist = dist
