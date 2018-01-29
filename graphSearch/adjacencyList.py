from collections import defaultdict
import sys


class Graph(object):
    def __init__(self, graph, directed=False):
        self._graph = graph
        self._directed = directed

    @classmethod
    def getGraph(cls):
        if len(sys.argv) == 1:
            FILE = raw_input("\nEnter the Edge List filename: ")
            directed = cls.isDirected()
            graph = cls.initialize(FILE, directed)
        elif len(sys.argv) == 2:
            FILE = sys.argv[1]
            directed = cls.isDirected()
            graph = cls.initialize(FILE, directed)
        return graph

    @classmethod
    def initialize(cls, FILE, directed):
        graph = defaultdict(set)
        with open(FILE, 'r') as f:
            for line in f:
                A, B = [int(vertex) for vertex in line.split()]
                graph[A].add(B)
        for key, values in graph.items():
            for value in values:
                if value not in graph:
                    graph[value] = set([])
                else:
                    pass
        return cls(graph, directed)

    @staticmethod
    def isDirected():
        while (True):
            directed = raw_input("Is the graph directed? ..y/n (enter Q/q to quit)\n>>").lower()
            if (directed == 'y'):
                directed = True
                break
            elif (directed == 'n'):
                directed = False
                break
            elif (directed == 'q'):
                sys.exit()
            else:
                print("Sorry, I didn't catch that..\n")
                pass
        return directed

    # input should be tuple or list of tuples
    # edge (undirected) arc (directed)
    def addEdge(self, connections):
        for node1, node2 in connections:
            self._add(node1, node2)

    def _add(self, node1, node2):
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        for n, cnxns in self._graph.iteritems():
            try:
                cnxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def getTranspose(self):
        graphT = defaultdict(set)
        for key in self._graph:
            graphT[key] = set([])
        for key, values in self._graph.items():
            if len(values) > 1:
                for value in values:
                    graphT[value].add(key)
            else:
                graphT[values[0]].add(key)
        return graphT