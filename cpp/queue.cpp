/* Compile and Run
```
cd dsa/cpp
g++ queue.cpp -o queue
./queue
```
*/
#include <iostream>
#include <queue>
#include <string>
#include <list>

// Default queue template definition
// template <class Type, class Container = deque<Type> > class queue;

// Custom queue
template <typename T>
using q = std::queue<T, std::deque<T>>;

using std::cout; using std::endl;
using std::queue; using std::string;

template <typename T>
void print(T queue) {
    int s = queue.size();
    for (int i = 0; i < s; i++) {
        cout << queue.front() << " --> ";
        queue.pop();
    }
    cout << "Empty queue" << endl;

}

int main() {
    // Using default queue, setting type = string
    cout << " -----------------" << endl;
    cout << " Default checkout queue" << endl;
    cout << " -----------------" << endl;
    queue<string> checkout;
    checkout.push("Hermione");
    checkout.push("Harry");
    checkout.push("Ron");
    checkout.push("Luna");
    print(checkout);
    cout << "There are " << checkout.size() << " people in the checkout queue" << endl;
    // Get top elem
    cout << "First in line is " << checkout.front() << endl;
    // Remove top elem
    checkout.pop();
    cout << "There are now " << checkout.size() << " people in the checkout queue" << endl;
    cout << "Next in line is " << checkout.front() << endl;

    // Vector custom queue
    cout << " -----------------" << endl;
    cout << " Custom Vector queue" << endl;
    cout << " -----------------" << endl;
    q<int> myq;
    for (int i = 0; i < 5; i++) {
        myq.push(i);
    }
    print(myq);
    cout << "Size: " << myq.size() << endl;
    cout << "Removing top element: " << myq.front() << endl;
    myq.pop();
    cout << "New top element: " << myq.front() << endl;

    return 0;
}

/* OUPUTS
 -----------------
 Default checkout queue
 -----------------
Hermione --> Harry --> Ron --> Luna --> Empty queue
There are 4 people in the checkout queue
First in line is Hermione
There are now 3 people in the checkout queue
Next in line is Harry
 -----------------
 Custom Vector queue
 -----------------
0 --> 1 --> 2 --> 3 --> 4 --> Empty queue
Size: 5
Removing top element: 0
New top element: 1
*/