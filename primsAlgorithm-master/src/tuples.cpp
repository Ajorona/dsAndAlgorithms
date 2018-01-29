#include "tuples.h"

Pair() {
    this->primary = 0;
    this->last = 0;
}

Pair(float primary, float last) {
    this->primary = primary;
    this->last = last;
}

Triple(float primary, float secondary, float last) {
    this->primary = primary;
    this->secondary = secondary;
    this->last = last;
}

Triple() {
    this->primary = 0;
    this->secondary = 0;
    this->last = 0;
}
