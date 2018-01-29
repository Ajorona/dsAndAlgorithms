#include <fstream>
#include<iostream>
#include <string>
#include <vector>

using namespace std;

class InputHandler
{
  public:
    vector<int> jobLengths;
    vector<int> jobWeights;
    InputHandler(string fileName);
    virtual ~InputHandler();
};

InputHandler::InputHandler(string fileName) {
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

InputHandler::~InputHandler()
{

}
