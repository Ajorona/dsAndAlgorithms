#include "graph.h"
#include "tuples.h"

//FUNCTION DEFINITIONS FOR ADJACENCY LIST

AdjListRow AdjListRow::getAdjListRow(vector<AdjListRow> adjacencyList, Triple u) {
  float key = u.primary;
  
  vector<AdjListRow>::iterator rowFinder = find_if( adjacencyList.begin(),
     adjacencyList.end(), [key] (const AdjListRow& row) { return row.headNode == key; });
  if (rowFinder != (adjacencyList.end())) {
    auto index = distance(adjacencyList.begin(), rowFinder);
      return adjacencyList.at(index);
  }
}

Pair AdjListRow::smallestWeight() {
  auto minimum = min_element(this->adjListBody.begin(), this->adjListBody.end(),
        [](const Pair &a, const Pair &b) {return a.weight < b.weight;});
  return *minimum;
}

void AdjListRow::addWeightedNode(float secondary, float weight) {
      this->adjListBody.push_back(Pair(secondary, weight));
}

AdjListRow::AdjListRow(float headNode, vector<Pair> adjListBody) {
  this->headNode = headNode;
  this->adjListBody = adjListBody;
}

AdjListRow::AdjListRow() {
  this->headNode = 0;
  this->adjListBody = {};
}

//FUNCTION DEFINITIONS FOR GRAPH CLASS

void Graph::graphMaker (string fileName) {
  ifstream infile(fileName);
  float nodes, edges, primary, secondary, weight, key;

  infile >> nodes >> edges;
  this->nodes = nodes;
  this->edges = edges;

  //get edges list from file
  for(float i = 0; i < edges; i++) {
  infile >> primary >> secondary >> weight;
  this->setEdge(primary, secondary, weight);
  }

  this->vertices.push_back(500);
  vector<Pair> adjListBody;
  vector<Triple>::iterator itr;
  for(itr = this->edgeList.begin(); itr != this->edgeList.end(); itr++) {
    if(find(this->vertices.begin(), this->vertices.end(), itr->primary) != this->vertices.end()) {
      continue;
    }
    else {
      this->vertices.push_back(itr->primary);
      this->adjacencyList.push_back(AdjListRow(itr->primary, adjListBody));
    }
  }
  this->adjacencyList.push_back(AdjListRow(500, adjListBody));

  //build adjacency list
  for(itr=(this->edgeList.begin()); itr != this->edgeList.end(); itr++) {
    key = itr->primary;

    vector<AdjListRow>::iterator rowChecker = find_if(
        this->adjacencyList.begin(), this->adjacencyList.end(),
            [key] (const AdjListRow& row) { return row.headNode == key; });

    if (rowChecker != this->adjacencyList.end()) {
        auto index = distance(this->adjacencyList.begin(), rowChecker);
            this->adjacencyList.at(index).addWeightedNode(itr->secondary, itr->weight);
    }
  }
}

static void Graph::outputAdjList() {
  vector<AdjListRow>::iterator itr;
  vector<Pair>::iterator it;

  ofstream output;
  output.open("output.txt");

  for(itr = graph.adjacencyList.begin(); itr != graph.adjacencyList.end(); itr++) {
    output << "u: " << itr->headNode << " ";
    for(it = itr->adjListBody.begin(); it != itr->adjListBody.end(); it++ ) {
      output << "v: " << it->vertex << " " << it->weight << " ";
    }
    output << endl;
  }
  output.close();
  return;
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

void Graph::setEdge(float primary, float secondary, float weight) {
  Triple edge(primary, secondary, weight);
  this->edgeList.push_back(edge);
}

float Graph::getNodes() {
  return this->nodes;
}

float Graph::getEdges() {
  return this->edges;
}
