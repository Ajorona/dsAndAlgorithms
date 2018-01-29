#include <iostream>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <iterator>
#include <string>
#include <map>
#include <queue>
#include <vector>

using namespace std;

//TUPLES

class WeightedVertex {
  public:
    float vertex;
    float weight;
    WeightedVertex();
    WeightedVertex(float, float);
};

class Edge {
  public:
    float nodeOne;
    float nodeTwo;
    float weight;
    Edge();
    Edge(float, float, float);
};

WeightedVertex::WeightedVertex() {
    this->vertex = 0;
    this->weight = 0;
}

WeightedVertex::WeightedVertex(float primary, float last) {
    this->vertex = primary;
    this->weight = last;
}

Edge::Edge() {
    this->nodeOne = 0;
    this->nodeTwo = 0;
    this->weight = 0;
}

Edge::Edge(float nodeOne, float nodeTwo, float weight) {
    this->nodeOne = nodeOne;
    this->nodeTwo = nodeTwo;
    this->weight = weight;
}

//END TUPLES
//BEGIN GRAPH

class AdjListRow
{
  public:
    vector<WeightedVertex> adjListBody;
    float headNode;

    void addWeightedNode(float, float);
    auto smallestWeight();
    AdjListRow(float, vector<WeightedVertex>);
    AdjListRow();

    static auto getAdjListRow(vector<AdjListRow>, Edge);
};

class Graph {
  private:
    float nodes;
    float edges;

  public:
    vector<Edge> edgeList;
    vector<AdjListRow> adjacencyList;
    vector<float> vertices;

    void setEdge(float, float, float);
    void graphMaker(string);
    AdjListRow adjacentNodes(float);
    void outputAdjList();
    float getNodes();
    float getEdges();
};

auto AdjListRow::getAdjListRow(vector<AdjListRow> adjacencyList, Edge u) {
  float key = u.nodeOne;
  
  vector<AdjListRow>::iterator rowFinder = find_if( adjacencyList.begin(),
     adjacencyList.end(), [key] (const AdjListRow& row) {return row.headNode == key;});

  if (rowFinder != (adjacencyList.end())) {
    auto index = distance(adjacencyList.begin(), rowFinder);
    return adjacencyList.at(index);
  }
}

auto AdjListRow::smallestWeight() {
  auto minimum = min_element(this->adjListBody.begin(), this->adjListBody.end(),
        [](const WeightedVertex &a, const WeightedVertex &b) {return a.weight < b.weight;});
  return *minimum;
}

void AdjListRow::addWeightedNode(float vertex, float weight) {
      this->adjListBody.push_back(WeightedVertex(vertex, weight));
}

AdjListRow::AdjListRow(float headNode, vector<WeightedVertex> adjListBody) {
  this->headNode = headNode;
  this->adjListBody = adjListBody;
}

AdjListRow::AdjListRow() {
  this->headNode = 0;
  this->adjListBody = {};
}

//FUNCTION DEFINITIONS FOR GRAPH CLASS

void Graph::graphMaker (string fileName) {
  vector<WeightedVertex> adjListBody;
  vector<Edge>::iterator itr;
  ifstream infile(fileName);

  float nodes, edges, nodeOne, nodeTwo, weight, key;

  infile >> nodes >> edges;
  this->nodes = nodes;
  this->edges = edges;

  for(float i = 0; i < edges; i++) {
  infile >> nodeOne >> nodeTwo >> weight;
  this->setEdge(nodeOne, nodeTwo, weight);
  }
  for(float i = 1; i <= nodes ; i++) {
    this->vertices.push_back(i);
    this->adjacencyList.push_back(AdjListRow(i, adjListBody));
  }

  //BUILD ADJACENCY LIST
  for(auto edgeItr = this->edgeList.begin(); edgeItr != this->edgeList.end(); edgeItr++) {
    vector<AdjListRow>::iterator uItr, vItr;
    nodeOne = edgeItr->nodeOne, nodeTwo = edgeItr->nodeTwo;

    uItr = find_if(this->adjacencyList.begin(), this->adjacencyList.end(),
        [nodeOne] (const AdjListRow& row) { return row.headNode == nodeOne; });
    vItr = find_if(this->adjacencyList.begin(), this->adjacencyList.end(),
        [nodeTwo] (const AdjListRow& row) { return row.headNode == nodeTwo; });

    if (uItr != this->adjacencyList.end()) {
        auto index = distance(this->adjacencyList.begin(), uItr);
        this->adjacencyList.at(index).addWeightedNode(edgeItr->nodeTwo, edgeItr->weight);
    }
    if (vItr != this->adjacencyList.end()) {
        auto index = distance(this->adjacencyList.begin(), vItr);
        this->adjacencyList.at(index).addWeightedNode(edgeItr->nodeOne, edgeItr->weight);
    }








  }
}

AdjListRow Graph::adjacentNodes(float head) {
  vector<AdjListRow>::iterator rowChecker = find_if(
    this->adjacencyList.begin(), this->adjacencyList.end(),
        [head] (const AdjListRow& row) {return row.headNode == head;});

  if (rowChecker != this->adjacencyList.end()) {
    auto index = distance(this->adjacencyList.begin(), rowChecker);
       return this->adjacencyList.at(index);
  }
  else {
      return adjacencyList.at(0);
  }
}

void Graph::setEdge(float nodeOne, float nodeTwo, float weight) {
  Edge edge(nodeOne, nodeTwo, weight);
  this->edgeList.push_back(edge);
}

float Graph::getNodes() {
  return this->nodes;
}

float Graph::getEdges() {
  return this->edges;
}

//END GRAPH
//BEGIN PRIM'S ALGORITHM

float getEdgeIndex(vector<Edge> primVector, float key) {
    auto it = find_if( primVector.begin(), primVector.end(),
        [key] (const Edge& edge) {return edge.nodeOne == key;});
    if (it != primVector.end()) {
        float index = distance(primVector.begin(), it);
        return index;
    } else {
      return INFINITY;
    }
}

struct WeightComparator {
  inline bool operator() (const Edge& a, const Edge& b)
  {
    return (a.weight < b.weight);
  }
};

struct VertexComparator {
  inline bool operator() (const Edge& a, const Edge& b) {
    {
      return (a.nodeOne < b.nodeOne);
    }
  }
};

vector<Edge> primsAlgorithm(Graph graph, float root) {
    vector<Edge> primVector;
    vector<Edge> minSpanningTree;
    Edge u, v;
    AdjListRow uAdj;
    float index;
    
    for(auto it = graph.vertices.begin(); it != graph.vertices.end(); it++) {
        u = Edge(*it, INFINITY, INFINITY);
        primVector.push_back(u);
    }
    index = getEdgeIndex(primVector, root);
    primVector.erase(primVector.begin()+index);
    primVector.insert(primVector.begin()+index, Edge(root, 0, 0));

    while(!primVector.empty()) {
        sort(primVector.begin(), primVector.end(), WeightComparator());
        u = primVector.at(0);
        primVector.erase(primVector.begin());
        minSpanningTree.push_back(Edge(u.nodeOne, u.nodeTwo, u.weight));

        uAdj = uAdj.getAdjListRow(graph.adjacencyList, u);
        for(auto it = uAdj.adjListBody.begin(); it != uAdj.adjListBody.end(); it++) {
            index = getEdgeIndex(primVector, it->vertex);
            if (index != INFINITY) {
              v = primVector.at(index);
              if(it->weight < v.weight) {
                v.nodeTwo = u.nodeOne;
                v.weight = it->weight;
                primVector.erase(primVector.begin()+index);
                primVector.insert(primVector.begin()+index, v);
              }
            }
        }
    }
  return minSpanningTree;
}

void outputMinSpanningTree(vector<Edge> minSpanningTree) {
    float sum = 0, vertexSum = 0, checkSum = 0;
    vector<Edge>::iterator itr;

    ofstream output;
    output.open("minSpanningTree.txt");

    sort(minSpanningTree.begin(), minSpanningTree.end(), VertexComparator());
    for(itr = minSpanningTree.begin(); itr != minSpanningTree.end(); itr++ ) {
      output << "(" << itr->nodeOne << ", " << itr->nodeTwo << ", " << itr->weight << ") " << endl;
      sum += itr->weight;
      vertexSum += itr->nodeOne;
    }
    for(int i = 0; i < 500; i++) { checkSum += i; }

    output << "the sum is:  " << fixed << sum << endl;
}

int main() {
    string fileString = "/home/aorona/workspace/cpp/PrimsAlgorithm/edges.txt";
    vector<Edge> minSpanningTree;
    Graph graph;
    graph.graphMaker(fileString);
    minSpanningTree = primsAlgorithm(graph, 1);
    outputMinSpanningTree(minSpanningTree);

    vector<AdjListRow>::iterator itr;
    vector<WeightedVertex>::iterator it;

    ofstream output;
    output.open("adjList.txt");

    for(itr = graph.adjacencyList.begin(); itr != graph.adjacencyList.end(); itr++) {
      output << "u: " << itr->headNode << " ";
      for(it = itr->adjListBody.begin(); it != itr->adjListBody.end(); it++ ) {
        output << "(v: " << it->vertex << ",w: " << it->weight << ")";
      }
      output << endl;
    }
    output.close();
}
