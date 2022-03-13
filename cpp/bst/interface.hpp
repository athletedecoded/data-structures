/* Inplace BST using references. This code was taken from @Eric Huber &
@Wade Fagen-Ulmschneider to improve my understanding of passing by reference
as opposed to passing by value. Passing references in C++ improves efficiency 
because it does not copy/duplicate values in memory and allows in place operations
*/

#pragma once

#include <stdexcept>
#include <utility>
#include <iostream>

template <typename K, typename D>
class BST {
  public:
    // Initialise with head = nullptr
    BST() : head_(nullptr) { }

    const D& find(const K& key); //takes key alias, returns data alias
    void insert(const K& key, const D& data);
    const D& remove(const K& key);

  private:
    class Node {
      public:
        const K& key; //immutable memory address of key
        const D& data; //immutable memory address of data

        Node* left; // pointer to left child
        Node* right; // pointer to right child

        // Initialise Node from key,data references --> key, data, null children
        Node(const K& key, const D& data)
          : key(key), data(data), left(nullptr), right(nullptr) { }
    };

    Node *head_; // root node ptr

    // Private fxns
    Node*& _find(const K& key, Node*& cur) const;
    const D& _remove(Node*& node);
    Node*& _get_predecessor(Node*& cur) const;
    Node*& _rightmost_of(Node*& cur) const;
    Node*& _swap_nodes(Node*& node1, Node*& node2);
 
  public:
    bool is_empty() const {
      return !head_;
    }

  private:
    void _printInOrder(Node* node) {
      if (!node) {
        std::cout << " ";
        return;
      }
      else {
        _printInOrder(node->left);
        std::cout << "[" << node->key << " : " << node->data << "]";
        _printInOrder(node->right);
      }
    }

  public:
    void printInOrder() {
      _printInOrder(head_);
    }

    void clear_tree() {
      while (head_) {
        remove(head_->key);
      }
    }
    // Destructor
    ~BST() {
      clear_tree();
    }

};

#include "implementation.hpp"