from collections import defaultdict
import sys, re

class Graph(object):
    def __init__(self, graph):
        self._graph = graph

    def __repr__(self):
        return 'a  weighted graph representation'

    @classmethod
    def getGraph(cls):
        if len(sys.argv) == 1:
            FILE = raw_input("\nEnter the Edge List filename: ")
            graph = cls.initialize(FILE)
        elif len(sys.argv) == 2:
            FILE = sys.argv[1]
            graph = cls.initialize(FILE)
        return graph

    @classmethod
    def initialize(cls, FILE):
        graph = defaultdict(list)
        with open(FILE, 'r') as f:
            for line in f:
                line = line.strip()
                raw_nodes = []
                key = int(line.split('\t', 1)[0])
                adj = line.split('\t', 1)[1]
                [raw_nodes.append(vertex) for vertex in re.split(r'\t+', adj)]

                w_nodes = []
                for vertex in raw_nodes:
                    A,B = vertex.split(',')
                    w_nodes.append((int(A),int(B)))

                [graph[key].append(node) for node in w_nodes]

        return cls(graph)

    def dijkstra(self,source):
        shortest_path = {node : float('inf') for node in list(self._graph.keys())}
        unvisited = {node : float('inf') for node in list(self._graph.keys())}
        shortest_path[source] = 0
        unvisited[source] = 0

        while unvisited:
            pin = min(unvisited, key=unvisited.get)
            unvisited.pop(pin, None)

            sorted_paths = sorted(self._graph[pin], key=lambda x: x[1])
            for i in xrange(len(sorted_paths)):
                path = sorted_paths[i]
                node = path[0]
                shortest_path[node] = min(shortest_path[node], 
                               (shortest_path[pin] + path[1]))
                if node in unvisited:
                    unvisited[node] = shortest_path[node]
        return shortest_path

def pull_paths(path_list, shortest_path):
    paths = []
    for val in path_list:
        path = shortest_path[val]
        paths.append(path)
    print paths

path_list = [7,37,59,82,99,115,133,165,188,197]
graph = Graph.getGraph()
shortest_path = graph.dijkstra(1)
pull_paths(path_list, shortest_path)



