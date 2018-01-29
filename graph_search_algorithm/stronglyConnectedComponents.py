from collections import defaultdict
import sys

#works on file with pairs of edges

class StronglyConnectedComponents(object):
    def __init__(self, graph, time=0, DFS_Map=None, 
                      DFS_T_Map=None, graphT=None):
        self.graph = graph
        self.time = time
        #Set DFS Map
        if DFS_Map is None:
            self.DFS_Map = {}
        else:
            self.DFS_Map = DFS_Map
        #Set DFS  T Map
        if DFS_T_Map is None:
            self.DFS_T_Map = {}
        else:
            self.DFS_T_Map = DFS_T_Map
        #Set graph transpose
        if graphT is None:
            graphT = defaultdict(set)
            for key, values in self.graph.items():
                if key not in graphT:
                    graphT[key] = set([])
                for value in values:
                    if value not in graphT:
                        graphT[value] = set([])
            for key, values in self.graph.items():
                for value in values:
                    graphT[value].add(key)
            self.graphT = graphT
        else:
            self.graphT = graphT

    def orderDFS(self):
        rawFinish = []
        for vertex in self.DFS_Map:
            attr = self.DFS_Map[vertex]
            f_time = attr['finish']
            elem = (vertex, f_time)
            rawFinish.append(elem)
        orderedFinish = sorted(rawFinish, key=lambda (k, val): val,
                                                      reverse=True)
        return orderedFinish

    def DFSSCC(self):
        for vertex in self.graph:
            self.DFS_Map[vertex] = {'color' : 'WHITE', 'prior' : None,
                                      'begin' : None, 'finish' : None}
        for vertex in self.DFS_Map:
            attr = self.DFS_Map[vertex]
            if attr['color'] == 'WHITE':
                self.DFS_VisitSCC(vertex)
        return self.DFS_Map

    def DFS_VisitSCC(self, vertex):
        self.time += 1
        attr = self.DFS_Map[vertex]
        attr['begin'] = self.time
        attr['color'] = 'GRAY'
        self.DFS_Map[vertex] = attr
        adjNodes = self.graph[vertex]
        for node in adjNodes:
            attr = self.DFS_Map[node]
            if attr['color'] == 'WHITE':
                attr['prior'] == vertex
                self.DFS_Map[node] = attr
                self.DFS_VisitSCC(node)
        attr = self.DFS_Map[vertex]
        attr['color'] = 'BLACK'
        self.time += 1
        attr['finish'] = self.time
        self.DFS_Map[vertex] = attr

    def DFS_TSCC(self, graphT, orderedFinish):

        for vertex in self.graphT:
            self.DFS_T_Map[vertex] = {'color' : 'WHITE', 'prior' : None,
                                        'begin' : None, 'finish' : None}
        sortCheck = []
        for vertex, f_time in orderedFinish:
            sortCheck.append(f_time)
            attr = self.DFS_T_Map[vertex]
            if attr['color'] == 'WHITE':
                self.DFS_T_VisitSCC(vertex)
        print sortCheck
        return self.DFS_T_Map

    def DFS_T_VisitSCC(self, vertex):
        self.time += 1
        attr = self.DFS_T_Map[vertex]
        attr['begin'] = self.time
        attr['color'] = 'GRAY'
        self.DFS_T_Map[vertex] = attr
        adjNodes = self.graph[vertex]
        for node in adjNodes:
            attr = self.DFS_T_Map[node]
            if attr['color'] == 'WHITE':
                attr['prior'] == vertex
                self.DFS_T_Map[node] = attr
                self.DFS_T_VisitSCC(node)
        attr = self.DFS_T_Map[vertex]
        attr['color'] = 'BLACK'
        self.time += 1
        attr['finish'] = self.time
        self.DFS_T_Map[vertex] = attr
