/* author @athletedecoded
Compile and Run
```
cd dsa/cpp
g++ array.cpp cube.cpp -o array
./array
```
*/

#include <iostream>
#include <vector>
#include "cube.h"
using std::cout; using std::endl;
using std::vector;
using obj::Cube;

void staticArray() {
    int vals[10];
    for (int i =0; i < 10; i++) {
        vals[i] = i*i;
    }
    // Find offset to 2nd item
    int offset = (long)&(vals[2]) - (long)&(vals);
    cout << "Memory offset to index 2: " << offset << endl;
    // Length of array
    int l = *(&vals + 1) - vals;
    cout << "Length: "<< l << endl;
    // Try add an 11th item --> Stack Smashing Error
    // vals[10] = 99;
}

void dynamicArray() {
    // Initialise dynamic array of cube objects
    vector<Cube> cubes {Cube(11), Cube(42), Cube(100)};
    // Inspect capactiy/size
    cout << "Initial capacity: " << cubes.capacity() << endl;
    cubes.push_back(Cube(800));
    cout << "New size: " << cubes.size() << endl;
    cout << "New capacity: " << cubes.capacity() << endl;

    // Find cube -- access by index
    Cube target = Cube(42);
    for (unsigned i = 0; i < cubes.size(); i++) {
        if (target == cubes[i]) {
            cout << "Found the target at index " << i << endl;
        }
    }

    //Access 3rd cube length by memory offset
    int size = sizeof(cubes[0]);
    Cube *c0 = &cubes[0] + 3;
    cout << c0->getLength() << endl;

}

int main() {
    cout << "------------------" << endl;
    cout << "** Static Array Demo **" << endl;
    staticArray();

    cout << "------------------" << endl;
    cout << "** Dynamic Array Demo **" << endl;
    dynamicArray();

    return 0;
}