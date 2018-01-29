#include <algorithm>
#include <fstream>
#include<iostream>
#include <iterator>
#include <string>
#include <vector>

using namespace std;

class InputHandler
{
  public:
    vector<int> jobLengths;
    vector<int> jobWeights;
    InputHandler(string fileName);
};

InputHandler::InputHandler(string fileName) {
    cout << fileName;
    int length = 0, weight = 0, inputSize = 0;
    ifstream infile(fileName);
    infile >> inputSize;
    for(int i=0; i < inputSize; i++)
    {
        infile >> length >> weight;
        jobLengths.push_back(length);
        jobWeights.push_back(weight);
    }
    cout << inputSize;
    cout << " job profiles created in InputHandler";
    cout << " instance" << endl;
}

int main()
{
  InputHandler jobs("jobs.txt");
  vector<int>::iterator itr;
  for (itr = jobs.jobLengths.begin(); itr != jobs.jobLengths.end(); ++itr)
      cout << *itr << ' ';
}
