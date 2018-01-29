    import math
    import random
    random.seed(None)

    # global variable to counter number of crossing edges
    global count
    count = []


    # get input file and transform into dictionary representing adjacency list
    # key = "head node", value = "adjacent nodes"
    def getGraph():
        graph = {}
        with open("input.txt", 'r') as f:
            for line in f:
                nodes = [int(vertex) for vertex in line.split()]
                graph[nodes[0]] = nodes[1:]
            return graph

    # Helper function to key for base case in recursion
    def getKey(dic):
        key = [i for i in dic]
        key = key[0]
        return key


    # By iterating this algorithm n times, a minimum cut may be found
    # with high probability. The Main function sets initial parameters
    # and passes them into to the recursing function.
    # keyChain tracks nodes as they are merged and deleted
    # marker sets the base value for merged nodes to be assigned so that
    # they do not overlap with the primary (unmerged nodes in the graph)
    def Main():
        global count
        i = 0
        graph = getGraph()
        n = int(math.pow(len(graph), 1) * math.log(len(graph)))
        while i < n:
            graph = getGraph()
            keyChain = range(1, 201)
            lowerBound = len(graph)
            marker = lowerBound + 1
            randomContraction(graph, lowerBound, marker, keyChain)
            i += 1

        print count
        print min(count)


    def randomContraction(graph, lowerBound, marker, keyChain):
        global count
        if (len(graph) == 2):
            key = getKey(graph)
            crossingEdges = len(graph[key])
            count.append(crossingEdges)
        else:
            keyA = random.choice(keyChain)
            adjNodesA = graph[keyA]
            while 1:
                keyB = random.choice(adjNodesA)
                if(keyB != keyA and keyB in keyChain):
                    break
            adjNodesB = graph[keyB]

            toMergeA = [keyA]
            toMergeB = [keyB]

            # create lists of merging nodes
            # and adjacent nodes
            mergedNodes = toMergeA + toMergeB
            adjNodes = adjNodesA + adjNodesB

            # delete unmerged representation of nodes
            del graph[keyA]
            del graph[keyB]
            keyChain.remove(keyA)
            keyChain.remove(keyB)

            #add representation of merged nodes
            keyChain.append(marker)
            graph[marker] = adjNodes

            # scrub any mention of unmerged nodes
            # from graph, replace with merged node
            # value
            for key, value in graph.items():
                for vertex in mergedNodes:
                    while (vertex in value):
                        temp = value
                        temp.remove(vertex)
                        temp.append(marker)
                        graph[key] = temp
            # remove any self-loops
            for vertex in mergedNodes:
                while (marker in adjNodes):
                    adjNodes.remove(marker)

            marker += 1
            randomContraction(graph, lowerBound, marker, keyChain)


    Main()


    '''
            if (indexA > lowerBound):
                toMergeA = lookupTable[indexA]
            else:
                toMergeA = [indexA]

            if (indexB > lowerBound):
                toMergeB = lookupTable[indexB]
            else:
                toMergeB = [indexB]
    '''
    '''
            scrubber = []
            if (keyA > lowerBound):
                toMergeA = lookupTable[keyA]
                scrubber.append(toMergeA)
            else:
                toMergeA = [keyA]

            if (keyB > lowerBound):
                toMergeB = lookupTable[keyA]
                scrubber.append(toMergeB)
            else:
                toMergeB = [keyB]
    '''