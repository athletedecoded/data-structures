/* Inplace BST using references. This code is from @Eric Huber &
@Wade Fagen-Ulmschneider to improve my understanding of passing by reference
as opposed to passing by value. Passing references in C++ improves efficiency 
because it does not copy/duplicate values in memory and allows in place operations
*/

#pragma once

#include "interface.hpp"

using std::runtime_error;
using std::swap;

/**
* find(key)
*/
template <typename K, typename D>
// Return type: alias of data
const D& BST<K, D>::find(const K& key) {
  Node*& node = _find(key, head_);
  if (node == nullptr) { throw runtime_error("error: key not found"); }
  return node->data;
}

template <typename K, typename D>
// Return type: BST<K, D>::Node*& == reference to a node pointer
typename BST<K, D>::Node*& BST<K, D>::_find(const K& key, Node*& cur) const {
  if (cur == nullptr) { return cur; }
  else if (key == cur->key) { return cur; }
  else if (key < cur->key) { return _find(key, cur->left); }
  else { return _find(key, cur->right); }
}

/**
* insert(key, data)
*/
template <typename K, typename D>
void BST<K, D>::insert(const K& key, const D& data) {
  // Find memory address of pointer to node with key
  Node *& node = _find(key, head_);
  // If node exists already with key
  if (node) { 
    throw runtime_error("Error: insert() used on an existing key"); 
  }
  node = new Node(key, data);
}

/**
* remove(key)
*/
template <typename K, typename D>
// Return type: alias of data
const D& BST<K, D>::remove(const K& key) {
  // Find memory address of pointer to node with key
  Node*& node = _find(key, head_);
  // If node with key not in tree
  if (!node) { 
    throw runtime_error("Error: remove() used on non-existent key"); 
  }
  return _remove(node);
}

template <typename K, typename D>
// Return type: alias of data
const D& BST<K, D>::_remove(Node*& node) {

  if (!node) { throw runtime_error("error: _remove() used on non-existent key"); }

  // If node is leaf:
  if (node->left == nullptr && node->right == nullptr) {
    // Create alias of data because once we delete node, 
    // which is a reference/alias of a pointer, the
    // data reference is unreliable (could hold any value)
    const D& data = node->data;
    delete node;
    node = nullptr;
    return data;
  }
  // Node has left child only
  else if (node->left != nullptr && node->right == nullptr) {
    const D& data = node->data;
    Node* temp = node;
    node = node->left;
    delete temp;
    return data;
  }
  // Node has right child only
  else if (node->left == nullptr && node->right != nullptr) {
    const D& data = node->data;
    Node* temp = node;
    node = node->right;
    delete temp;
    return data;
  }
  // Node has two children
  else {
    // Find the predecessor of the current node.
    Node*& pred = _get_predecessor(node);
    if (!pred) {
      throw runtime_error("error: predecessor not found");
    }
    Node*& moved_node = _swap_nodes(node, pred);
    return _remove(moved_node);
  }
}

// -------
// _get_predecessor: You pass in a pointer to a node, and it returns a reference
// to the pointer to the predecessor node. If the predecessor does not exist,
// it returns a reference to a node pointer == nullptr. The predecessor is the right
// most child of the node's left subtree
template <typename K, typename D>
typename BST<K, D>::Node*& BST<K, D>::_get_predecessor(
  Node*& cur) const {

  if (!cur) {
    return cur;
  }
  
  if (!(cur->left)) {
    return cur->left;
  }

  return _rightmost_of(cur->left);
}

// _rightmost_of:
template <typename K, typename D>
typename BST<K, D>::Node*& BST<K, D>::_rightmost_of(
  Node*& cur) const {
  if (!cur) return cur;
  if (!(cur->right)) return cur;
  return _rightmost_of(cur->right);
}

// _swap_nodes: swap node and predecessor
template <typename K, typename D>
typename BST<K, D>::Node*& BST<K, D>::_swap_nodes(
  Node*& node, Node*& pred) {

  Node* track_node = node;
  Node* track_pred = pred;

  if (node->left == pred) {
    swap(node->right, pred->right);
    node->left = track_pred->left;
    track_pred->left = node;
    node = track_pred;
    return node->left;
  }
  else if (node->right == pred) {
    swap(node->left, pred->left);
    node->right = track_pred->right;
    track_pred->right = node;
    node = track_pred;
    return node->right;
  }
  else if (pred->left == node) {
    swap(pred->right, node->right);
    pred->left = track_node->left;
    track_node->left = pred;
    pred = track_node;
    return pred->left;
  }
  else if (pred->right == node) {
    swap(pred->left, node->left);
    pred->right = track_node->right;
    track_node->right = pred;
    pred = track_node;
    return pred->right;
  }
  else {

    swap(node->left, pred->left);
    swap(node->right, pred->right);
    swap(node, pred);

    return pred;
  }

}