from collections import defaultdict
import sys

def getGraph():
    if len(sys.argv) == 1:
        FILE = raw_input("enter the adjacency list filename: ")
        FILE = sys.argv[0]
        while (True):
            directed = raw_input("Is the graph directed? ..y/n (enter Q/q to quit)").lower()
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
        graph = Graph.initialize(FILE, directed)
    elif len(sys.argv) == 2:
        FILE = sys.argv[0]
        directed = sys.argv[1]
        graph = Graph.initialize(FILE, directed)


class Graph(object):
    def __init__(self, graph, directed=False):
        self._graph = graph
        self._directed = directed

    # take file input and initialize graph object with file data
    @classmethod
    def initialize(cls, FILE, directed):
        graph = defaultdict(set)
        with open(FILE, 'r') as f:
            for line in f:
                nodes = [int(vertex) for vertex in line.split()]
                graph[nodes[0]] = nodes[1:]
        return cls(graph, directed)

    # transpose graph
    def getTranspose(self):
        graphT = defaultdict(set)
        for key in self._graph: 
            graphT[key] = set([])
        for key, values in self._graph:
            for value in values:
                graphT[value].append(key)
        return graphT


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

    # Breadth-First Search
    def BFS(origin):
        BFS_Map = {}
        for vertex in self._graph:
            BFS_Map[vertex] = {'color' : 'WHITE', 'distance' : None, 'prior' : None}
        BFS_Map[origin] = {'color' : 'GRAY', 'distance': 0, 'prior' : None}
        queue = [origin]

        while len(queue) > 0:
            u = queue.pop(0)
            for vertex in self._graph[u].values():
                attr = BFS_Map[vertex].values()
                if attr['color'] == 'WHITE':
                    attr['distance'] = u[distance] + 1
                    attr['color'] = 'GRAY'
                    attr['prior'] = u
                    BFS_Map[vertex] = attr
                    queue.append(vertex)
                attr = BFS_Map[u].values()
                attr['color'] = 'BLACK'
                BFS_Map[u] = attr
        return BFS_Map

    def DFS():
        time = 0
        DFS_Map = {}
        for vertex in self._graph:
            DFS_Map[vertex] = {'color' : 'WHITE', 'prior' : None,
                                 'begin' : None, 'finish' : None}
        for vertex in DFS_Map:
            attr = DFS_Map[vertex]
            if attr['color'] == 'WHITE':
                DFS_Visit(vertex)

        return DFS_Map

    def DFS_Visit(vertex):
        time += 1
        attr = DFS_Map[vertex]
        attr['begin'] = time
        attr['color'] = 'GRAY'
        DFS_Map[vertex] = attr
        adjNodes = self._graph[vertex].values()
        for node in adjNodes:
            attr = DFS_Map[node]
            if attr['color'] == 'WHITE':
                attr['prior'] == vertex
                DFS_Map[vertex] = attr
                DFS_Visit[vertex]
        attr = DFS_Map[vertex]
        attr['color'] == 'BLACK'
        time += 1
        attr['finish'] == time
        DFS_Map[vertex] = attr

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


Main()
