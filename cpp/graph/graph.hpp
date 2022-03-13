/* author @athletedecoded */
#pragma once
#include <iostream>
#include <string>
#include <vector>
#include <tuple>
#include <map>
#include <queue>

using namespace std;

// Define node struct containing value and next pointer
struct Vertex
{
  int val;
  bool explored = false;
  Vertex* parent;
};

using Edge = tuple<int, int>;
using Frontier = queue<Vertex*, deque<Vertex*>>;

// Define graph class
class Graph {
  private:
    vector<Vertex> v_; // vertices
    vector<Edge> e_; // Edge pairs
    bool undirected_;

  public:
    // Initialise graph using vertices and Edges
    Graph(vector<Vertex> v, vector<Edge> e, bool undirected) {
      v_ = v;
      e_ = e;
      undirected_ = undirected;
    }

    // Insert vertex
    void insert_vx(int val) {
      Vertex v; 
      v.val = val;
      cout << "Inserting vertex: " << v.val << endl;
      v_.push_back(v);
    }

    // Insert Edge
    void insert_edge(Edge e) {
      cout << "Inserting Edge: " << get<0>(e) << "," << get<1>(e) << endl;
      e_.push_back(e);
    }

    // Reset nodes
    void reset_nodes() {
      for (int i = 0; i < v_.size(); i++ ) {
        v_[i].explored = false;
        v_[i].parent = nullptr;
      }
    } 

    // Return all vertices
    vector<Vertex> get_vertices() {
      return v_;
    }

    // Return all Edges
    vector<Edge> get_edges() {
      return e_;
    }

    // Return adjacency map
    map<int, vector<int>> get_map() {
      return adjacency_map();
    }

    // Create adjacency map
    map<int, vector<int>> adjacency_map() {
      // Ref to the Graph vectors
      vector<Vertex>& v = v_;
      vector<Edge>& e = e_;
       // Init adj_map
      map<int, vector<int>> m;
      // Iterate through vertices
      for (int i = 0; i<v.size(); i ++) {
        // Dereference
        m[v[i].val];
      }
      // Iterate through Edges
      for (int i = 0; i<e.size(); i++) {
        // 1st tuple element = key, 2nd = add to adjacency list
        m[get<0>(e[i])].push_back(get<1>(e[i]));
        if (undirected_) {
          // Add inverse edge
          m[get<1>(e[i])].push_back(get<0>(e[i]));
        }
      }
      return m;
    }

    void print_map() {
      // iterate
      cout << "Adjacency Map" << endl;
      map<int, vector<int>> m = adjacency_map();
      for (auto itr = m.begin(); itr != m.end(); ++itr) {
        //dereference iterator (equivalent forms)
        int k = itr->first;
        cout << "k: " << k;
        vector<int> v = itr->second;
        cout << ", v: [";
        for (int i = 0; i<v.size(); i++) {
          cout << v[i] << ",";
        }
        cout << "]" << endl;
      }
    }

    Vertex bfs(int src, int tgt) {
      map<int, vector<int>> m = get_map();
      Frontier f;
      // Set src node parent to nullptr
      v_[src].parent = nullptr;
      // Push into frontier: pointer to src node
      f.push(&v_[src]);

      while (f.size() != 0) {
        // Get pointer to next node from frontier
        Vertex* node = f.front();
        f.pop();
        // If node pointer == target address
        if (node == &v_[tgt]) {
          cout << "Found the target node" << endl;
          return *node;
        }
        // Else mark explored
        node->explored = true;
        // Get neighbours
        if ( m.find(node->val) != m.end()) {
          vector<int> nbs = m[node->val];
          for (int i = 0; i < nbs.size(); i++) {
            // If neighbour not explored
            if (v_[nbs[i]].explored == false) {
              // Set neighbour.parent to point at curr node
              v_[nbs[i]].parent = node;
              // Add neighbour pointer to frontier
              f.push(&v_[nbs[i]]);
            }
          }
        }
      }
      // if target not found, return src
      cout << "Target node not found" << endl;
      return v_[src];
    }

    void dfs(int src) {
      map<int, vector<int>> m = get_map();
      Vertex* node = &v_[src];
      node->explored = true;
      // Get neighbours
      if ( m.find(node->val) != m.end()) {
        vector<int> nbs = m[node->val];
        // For each neighbour
        for (int i = 0; i < nbs.size(); i++) {
          // If neighbour not explored
          if (v_[nbs[i]].explored == false) {
            // Set neighbour.parent to point at curr node
            v_[nbs[i]].parent = node;
            // recurse along the path of neighbour
            dfs(nbs[i]);
          }
        }
      }
    }

    vector<int> reachable(int src) {
      // Reset graph state
      reset_nodes();
      // Call DFS
      dfs(src);
      // Check which nodes have been explored
      vector<int> reached;
      for (int i = 0; i < v_.size(); i++ ) {
        if (v_[i].explored && v_[i].val != src) {
          reached.push_back(v_[i].val);
        }
      }
      return reached;
    }
   
    void print_path(Vertex node) {
      vector<int> path;
      path.push_back(node.val);
      // Follow parent pointers
      while (node.parent != nullptr) {
        Vertex p = *(node.parent);
        path.push_back(p.val);
        node = *(node.parent);
      }
      // Print path (reverse)
      cout << "START --> ";
      for (int i = path.size() - 1; i >= 0; i--) {
        cout << path[i] << " --> ";
      }
      cout << "END" << endl;
    }
};

