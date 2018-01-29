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
                print("Sorry, I didn't catch that..")
                pass
        graph = Graph.initialize(FILE, directed)
    elif len(sys.argv) == 2:
        FILE = sys.argv[1]
        directed = sys.argv[2]
        graph = Graph.initialize(FILE, directed)
    print graph._graph

getGraph()