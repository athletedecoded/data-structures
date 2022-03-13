/* author @athletedecoded
Compile and Run
```
cd dsa/cpp/llist
make
./llist
```
*/

#include <iostream>
#include "llist.hpp"

using std::cout; using std::endl;

int main() {
  List list;

  list.traverse();
  list.insertFront(3);
  list.insertFront(6);
  list.insertEnd(9);
  list.insertEnd(12);
  list.insertEnd(15);
  list.insertFront(1);
  cout << "length " << list.getLength() << endl;
  list.traverse();
  list.deleteFront();
  list.deleteEnd();
  list.insertAt(3, 7);
  list.insertAt(7, 3);
  list.traverse();
  list.deleteAt(2);
  cout << "length " << list.getLength() << endl;
  list.traverse();
  Node* n = list.find(3);
  cout << n << endl;
  Node* m = list.find(113);

  return 0;
}

/* OUTPUTS:
This list is empty!
length 6
1 --> 6 --> 3 --> 9 --> 12 --> 15 --> nullptr
Deleting 1
Deleting 15
Can't insert at idx = 7. Index must be between 0 and 5
6 --> 3 --> 9 --> 7 --> 12 --> nullptr
Deleting 9
length 4
6 --> 3 --> 7 --> 12 --> nullptr
Found node at idx = 1
0x55bd332cd2c0
No value 113 in the list
*/