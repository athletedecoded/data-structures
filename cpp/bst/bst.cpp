/*
Compile and Run
```
cd dsa/cpp/bst
make
./bst
```
*/

#include <string>
#include <iostream>
#include <vector>

#include "interface.hpp"

using std::string; using std::cout;
using std::endl; using std::vector;

int main() { 
  
  const int V_SIZE = 8;
  vector<int> v(V_SIZE, 0); // create 0 vector of 8 elements
  vector<string> s = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven"};
  // Reassign each item to hold a value matching its index
  for (int i=0; i<V_SIZE; i++) {
    v[i] = i*i;
  }

  // Memory scope for tree
  {
    BST<int, string> tree;

    cout << std::boolalpha;
    cout << "Dictionary empty? " << tree.is_empty() << endl;

    cout << "Inserting items..." << endl;

    // Insert items
    for (int i = 0; i < 8; i++) {
      tree.insert(v[i], s[i]);
    }

    cout << "Dictionary empty? " << tree.is_empty() << endl;

    cout << "In order traversal:" << endl;
    tree.printInOrder();
    cout << endl;

    cout << "tree.find(9): " << tree.find(9) << endl;

    cout << "tree.remove(9): " << tree.remove(9) << endl;
    cout << "tree.remove(0): " << tree.remove(0) << endl;
    try {
      cout << "tree.remove(2): " << tree.remove(2) << endl;
    }
    catch (const runtime_error& e) {
      cout << "Caught exception with error message: " << e.what() << endl;
    }

    cout << "In order traversal:" << endl;
    tree.printInOrder();
    cout << endl;

    try {
      cout << "tree.find(9): " << tree.find(9) << endl;
    }
    catch (const runtime_error& e) {
      cout << "Caught exception with error message: " << e.what() << endl;
    }

  cout << "Exiting program normally." << endl;
  
  return 0;
  }

}
