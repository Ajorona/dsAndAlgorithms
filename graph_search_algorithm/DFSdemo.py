    from functools import wraps
    import inspect

    class DepthFirstSearch(object):
        @initializer
        def __init__(self, graphObj, time, DFS_Map)
            self.graph = graphObj._graph
            self.time = time
            self.DFS_Map = DFS_Map

        def initializer(func):
            names, varargs, keywords, defaults = inspect.getargspec(func)
            @wraps(func)
            def wrap(self, *args):
                setattr(self, names[2], 0)
                setattr(self, names[3], {})
                func(self, *args)
            return wrap

    def DFS(self):
        for vertex in self.graph:
            self.DFS_Map[vertex] = {'color' : 'WHITE', 'prior' : None,
                                      'begin' : None, 'finish' : None}
        for vertex in self.DFS_Map:
            attr = self.DFS_Map[vertex]
            if attr['color'] == 'WHITE':
                DFS_Visit(vertex)
        return self.DFS_Map

    def DFS_Visit(self, vertex):
        time += 1
        attr = self.DFS_Map[vertex]
        attr['begin'] = time
        attr['color'] = 'GRAY'
        self.DFS_Map[vertex] = attr
        adjNodes = self.graph[vertex]
        for node in adjNodes:
            attr = self.DFS_Map[node]
            if attr['color'] == 'WHITE':
                attr['prior'] == vertex
                self.DFS_Map[vertex] = attr
                self.DFS_Visit[vertex]
        attr = self.DFS_Map[vertex]
        attr['color'] == 'BLACK'
        time += 1
        attr['finish'] == time
        self.DFS_Map[vertex] = attr