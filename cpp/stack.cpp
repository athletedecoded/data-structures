/* author @athletedecoded
Compile and Run
```
cd dsa/cpp
g++ stack.cpp -o stack
./stack
```
*/
#include <iostream>
#include <stack>
#include <string>
#include <list>

// Default stack template definition
// template <class Type, class Container = deque<Type> > class stack;

// Custom modified stacks
using ListofIntsStack = std::stack<int, std::list<int>>;

template <typename T>
using VectorStack = std::stack<T, std::list<T>>;

using std::cout; using std::endl;
using std::stack; using std::string;

template <typename T>
void printStack(T stack) {
    int s = stack.size();
    for (int i = 0; i < s; i++) {
        cout << stack.top() << " --> ";
        stack.pop();
    }
    cout << "Empty stack" << endl;

}

int main() {
    // Using default stack, setting type = string
    cout << " -----------------" << endl;
    cout << " Default pancake stack" << endl;
    cout << " -----------------" << endl;
    stack<string> pancakes;
    pancakes.push("Blueberry");
    pancakes.push("Choccie Chip");
    pancakes.push("Banana");
    printStack(pancakes);
    cout << "There are " << pancakes.size() << " pancakes in the stack" << endl;
    // Get top elem
    cout << "Top pancake is " << pancakes.top() << endl;
    cout << "There are still " << pancakes.size() << " pancakes in the stack" << endl;
    // Remove top elem
    pancakes.pop();
    cout << "Yummo..there are now " << pancakes.size() << " pancakes in the stack" << endl;
    cout << "Top pancake is now " << pancakes.top() << endl;

    // List of ints custom stack
    cout << " -----------------" << endl;
    cout << " Custom List of Ints Stack" << endl;
    cout << " -----------------" << endl;
    ListofIntsStack ints;
    for (int i = 0; i <5; i++) {
        ints.push(i);
    }
    printStack(ints);
    cout << "Size: " << ints.size() << endl;
    cout << "Removing top element: " << ints.top() << endl;
    ints.pop();
    cout << "New top element: " << ints.top() << endl;

    // Vector custom stack
    cout << " -----------------" << endl;
    cout << " Custom Vector Stack" << endl;
    cout << " -----------------" << endl;
    VectorStack<int> vstack;
    for (int i = 0; i < 5; i++) {
        vstack.push(i+10);
    }
    printStack(vstack);
    cout << "Size: " << vstack.size() << endl;
    cout << "Removing top element: " << vstack.top() << endl;
    vstack.pop();
    cout << "New top element: " << vstack.top() << endl;

    return 0;
}

/* OUPUTS
 -----------------
 Default pancake stack
 -----------------
Banana --> Choccie Chip --> Blueberry --> Empty stack
There are 3 pancakes in the stack
Top pancake is Banana
There are still 3 pancakes in the stack
Yummo..there are now 2 pancakes in the stack
Top pancake is now Choccie Chip
 -----------------
 Custom List of Ints Stack
 -----------------
4 --> 3 --> 2 --> 1 --> 0 --> Empty stack
Size: 5
Removing top element: 4
New top element: 3
 -----------------
 Custom Vector Stack
 -----------------
14 --> 13 --> 12 --> 11 --> 10 --> Empty stack
Size: 5
Removing top element: 14
New top element: 13
*/