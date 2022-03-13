/* author @athletedecoded */
#pragma once
#include <iostream>
#include <string>

using std::cout; using std::endl;
using std::string;
// Define node struct containing value and next pointer
struct Node
{
  int val;
  Node* next;
};

// Define singly linked list class with tail and head
class List {
  private:
    Node* head_; // head pointer
    Node* tail_; // tail pointer
    int length_; // length
  public:
    // Constructor --> initialise list with head and tail as nullptr
    List() {
      head_ = nullptr;
      tail_ = nullptr;
    }
    int getLength();
    bool isEmpty();
    void traverse();
    void insertFront(int val);  
    void insertEnd(int val);  
    void insertAt(int idx, int val);  
    int deleteFront();  
    int deleteEnd(); 
    void deleteAt(int idx); 
    Node* find(int val); 
};

int List::getLength() {
  return length_;
}
/*
Insert node at front of the list
 */
void List::insertFront(int val) {
  // Create a new Node on heap memory
  Node *node = new Node;
  // Assign val to node
  node->val = val;
  // If this is 1st node
  if(head_==nullptr) {
    tail_ = node; //point tail at node
    node->next = nullptr;
  } 
  node->next = head_; // Point node at current head
  head_ = node; //point head at node
  // Increment list length
  length_ ++;
}

/*
Insert node at end of the list
 */
void List::insertEnd(int val) {
  // Create a new Node on heap memory
  Node *node = new Node;
  // Assign val to node
  node->val = val;
  // If this is 1st node
  if(head_==nullptr) {
    head_ = node; //point head at node  
  }
  tail_->next = node;
  node->next = nullptr;
  tail_ = node; //point tail at node
  // Increment list length
  length_ ++;
}

/*
Insert node at idx position
 */
void List::insertAt(int idx, int val) {
  // Check idx position within length of list
  if(idx < List::getLength()) {
    // Create a new Node on heap memory
    Node* node = new Node;
    // Assign val to node
    node->val = val;
    // If this is 1st node
    if(head_==nullptr) {
      head_ = node; //point head at node
      tail_ = node; //point tail at node 
      node->next = nullptr;
    }
    // Traverse until idx position
    Node* curr = head_;
    Node* prev = nullptr;
    for(int i = 0; i < idx; i++) {
      prev = curr;
      curr = curr->next;
    }
    //Assign pointers
    prev->next = node;
    node->next = curr;
    // Increment list length
    length_ ++;
  } else {
      cout << "Can't insert at idx = " << idx;
      cout << ". Index must be between 0 and " << List::getLength() << endl;
  }
}

/*
Delete node at front of the list
 */
int List::deleteFront() {
  if(List::isEmpty()) {
    cout << "Can't delete from an empty list!" << endl;
    return 1;
  }
  // Copy head node to tmp_node variable
  Node* curr = head_;
  head_ = head_->next; //shift head pointer to next node
  cout << "Deleting " << curr->val << endl;
  delete curr;
  curr = nullptr; //good convention, even if in stack memory
  // Decrement list length
  length_ --;
  return 0;
}

/*
Delete node at end of the list
Recall of singly linked list, we will have to first traverse list from start
 */
int List::deleteEnd() {
  if(List::isEmpty()) {
    cout << "Can't delete from an empty list!" << endl;
    return 1;
  }
  Node* curr = head_;
  Node* prev = nullptr;
  while (curr != tail_) {
    prev = curr;
    curr = curr->next;
  }
  // On terminating loop, node->next = nullptr
  prev->next = nullptr;
  tail_ = prev;
  cout << "Deleting " << curr->val << endl;
  delete curr;
  curr = nullptr; //good convention, even if in stack memory
  // Decrement list length
  length_ --;
  return 0;
}

/*
Delete node at idx position
*/
void List::deleteAt(int idx) {
  // Check idx position within length of list
  if(idx < List::getLength()) {
    // Traverse until idx position
    Node* curr = head_;
    Node* prev = nullptr;
    for(int i = 0; i < idx; i++) {
      prev = curr;
      curr = curr->next;
    }
    //Assign pointers
    prev->next = curr->next;
    cout << "Deleting " << curr->val << endl;
    delete curr;
    curr = nullptr;
    // Increment list length
    length_ --;
  } else {
      cout << "Can't delete idx = " << idx;
      cout << ". Index must be between 0 and " << List::getLength() << endl;
  }
}

/*
Print the list while traversing
 */
void List::traverse() {
  if(List::isEmpty()) {
    cout << "This list is empty!" << endl;
  } else {
  Node *ptr = head_;
    while (ptr != nullptr) {
      cout << ptr->val << " --> ";
      ptr = ptr->next;
    }
    cout << "nullptr" << endl;
  }
}

/*
Check if list is empty
 */
bool List::isEmpty() {
  if(head_==nullptr) {
    return true;
  }
  return false;
}

/*
Find node containing val
 */
Node* List::find(int val) {
  Node *ptr = head_;
  int idx = 0;
  while (ptr != nullptr) {
    if (ptr->val == val) { 
      cout << "Found node at idx = " << idx << endl;
      return ptr; 
    }
    ptr = ptr->next;
    idx ++;
  }
  cout << "No value " << val << " in the list" << endl;
  return nullptr;  
}
