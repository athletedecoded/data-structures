/* author @athletedecoded */

#include <iostream>
#include <cmath>
#include "cube.h"

using std::cout; using std::endl;
namespace obj {
    // Single parameter constructor
    Cube::Cube(double length) {
        length_ = length;
    }
    bool Cube::operator==(const Cube & other) {
        return (length_ == other.length_);
    }
    int Cube::getLength() const{
        return length_;
    }
    double Cube::getVolume() const{
        return pow(length_,3);
    }
    double Cube::getSurfaceArea() const{
        return 6 * pow(length_,2);
    }
    void Cube::setLength(double length) {
        length_ = length;
    }
}