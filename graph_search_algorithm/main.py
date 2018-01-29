from collections import defaultdict
import sys

from adjacencyList import Graph
from depthFirstSearch import DepthFirstSearch
from stronglyConnectedComponents import StronglyConnectedComponents
from graphSearch import BFS


#DFS of Graph object and descending list of finish time
graphObj = Graph.getGraph()
graph = graphObj._graph
print graph

SCC = StronglyConnectedComponents(graph)
graphT = SCC.graphT
print graphT


"""
DFS_Map = SCC.DFSSCC()
orderedFinish = SCC.orderDFS()


#Get graph transpose from SCC class

DFS_T_Map = SCC.DFS_TSCC(graphT, orderedFinish)

print DFS_T_Map
"""