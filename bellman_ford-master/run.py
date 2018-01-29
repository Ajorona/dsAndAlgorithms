from graph_maker import Graph
from floyd_warshall import Run_Floyd_Warshall_Algorithm

graph = Graph("input/g3.txt")

floyd_warshall = Run_Floyd_Warshall_Algorithm(graph)

def find_shortest_shortest_path(graph, floyd_warshall):
    dist = floyd_warshall.dist
    ssp = float("Inf")
    for i in range(graph.total_vertices):
        for j in range(graph.total_vertices):
            if dist[i][j] < ssp:
                ssp = dist[i][j]
    return ssp

print find_shortest_shortest_path(graph, floyd_warshall)
