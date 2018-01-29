from graph_maker import Graph

class Run_Bellman_Ford_Algorithm():
    def __init__(self, adjacency_list, source_vertex):
        bellman_path = {}
        has_negative_cycle = False
        # [distance, weight]
        for vertex in adjacency_list.vertex_list:
            bellman_path[vertex] = [float("Inf"), float("Inf")]
        bellman_path[source_vertex] = [0, float("Inf")]

        for i in xrange(0, adjacency_list.total_vertices):
            for edge in adjacency_list.edge_list:
                u, v, weight = edge
                comparator_weight = bellman_path[u][0] + weight
                if bellman_path[v][0] > comparator_weight:
                    bellman_path[v][0] = comparator_weight
                    bellman_path[v][1] = u

        for edge in adjacency_list.edge_list:
            u, v, weight = edge
            if bellman_path[v][0] > bellman_path[u][0] + weight:
                has_negative_cycle = True

        self.bellman_path = bellman_path
        self.has_negative_cycle = has_negative_cycle
