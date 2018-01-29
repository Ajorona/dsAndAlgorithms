#ifndef GRAPH H
#define GRAPH_H

class Graph {
  private:
    float nodes;
    float edges;

  public:
    vector<Triple> edgeList;
    vector<AdjListRow> adjacencyList;
    vector<float> vertices;

    void setEdge(float, float, float);
    void graphMaker(string);
    AdjListRow adjacentNodes(float);

    static void outputAdjList();
};


class AdjListRow
{
  public:
    vector<Pair> adjListBody;
    float headNode;

    AdjListRow(float, vector<Pair>);
    void addWeightedNode(float, float);
    Pair smallestWeight();

    static AdjListRow getAdjListRow(vector<AdjListRow>, Triple)
};

#endif