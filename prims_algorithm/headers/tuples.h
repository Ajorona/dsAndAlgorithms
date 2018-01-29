#ifndef TUPLES H
#define TUPLES_H

//vertex, weight are now primary last
//node1 is now primary, node2 is now secondary, weight is now last

class Pair {
  public:
    float primary;
    float last;
};

class Triple {
  public:
    float primary;
    float secondary;
    float last;
};

struct  LessThanByWeight {
  bool operator()(const Triple& lhs, const Triple& rhs)
  {
    return lhs.last > rhs.last;
  }
};

#endif
