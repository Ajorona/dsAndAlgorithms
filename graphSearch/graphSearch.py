def BFS(origin, graphObj):
    graph = graphObj._graph
    BFS_Map = {}
    for vertex in graph:
        BFS_Map[vertex] = {'color' : 'WHITE', 'distance' : None, 'prior' : None}
    BFS_Map[origin] = {'color' : 'GRAY', 'distance': 0, 'prior' : None}
    queue = [origin]

    while len(queue) > 0:
        u = queue.pop(0)
        for vertex in graph[u]:
            attr = BFS_Map[vertex]
            if attr['color'] == 'WHITE':
                parent = BFS_Map[u]
                attr['distance'] = parent['distance'] + 1
                attr['color'] = 'GRAY'
                attr['prior'] = u
                BFS_Map[vertex] = attr
                queue.append(vertex)
            attr = BFS_Map[u]
            attr['color'] = 'BLACK'
            BFS_Map[u] = attr
    return BFS_Map


"""
def __str__(self):
    return '{}({})'.format(self.__class__.__name__, dict(self._graph))
"""