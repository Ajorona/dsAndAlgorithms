class DepthFirstSearch(object):
    def __init__(self, graph, time=0, graphT=None, DFS_Map=None):
        self.graph = graph
        self.time = time
        #Set DFS Map
        if DFS_Map is None:
            self.DFS_Map = {}
        else:
            self.DFS_Map = DFS_Map
        #Set graph transpose
        if graphT is None:
            graphT = defaultdict(set)
            for key in self.graph:
                graphT[key] = set([])
            for key, values in self._graph.items():
                if len(values) > 1:
                    for value in values:
                        graphT[value].add(key)
                else:
                    graphT[values[0]].add(key)
        else:
            self.graphT = graphT

    def DFS(self):
        for vertex in self.graph:
            self.DFS_Map[vertex] = {'color' : 'WHITE', 'prior' : None,
                                      'begin' : None, 'finish' : None}
        for vertex in self.DFS_Map:
            attr = self.DFS_Map[vertex]
            if attr['color'] == 'WHITE':
                self.DFS_Visit(vertex)
        return self.DFS_Map

    def DFS_Visit(self, vertex):
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
                self.DFS_Visit(node)
        attr = self.DFS_Map[vertex]
        attr['color'] = 'BLACK'
        self.time += 1
        attr['finish'] = self.time
        self.DFS_Map[vertex] = attr

    def DFS_T(self, gsubT, orderedFinish):
        DFS_T_Map = {}
        for vertex in gsubT:
            DFS_T_Map[vertex] = {'color' : 'WHITE', 'prior' : None,
                                      'begin' : None, 'finish' : None}
        sortCheck = []
        for vertex, f_time in orderedFinish:
            sortCheck.append(f_time)
            attr = DFS_T_Map[vertex]
            if attr['color'] == 'WHITE':
                self.DFS_T_Visit(vertex)
        print sortCheck
        return DFS_T_Map

    def DFS_T_Visit(self, vertex):
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
                self.DFS_Visit(node)
        attr = self.DFS_Map[vertex]
        attr['color'] = 'BLACK'
        self.time += 1
        attr['finish'] = self.time
        self.DFS_Map[vertex] = attr
