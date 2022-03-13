/* author @athletedecoded
Compile and Run
```
cd dsa/cpp/graph
make
./graph
```
*/

#include <iostream>
#include "graph.hpp"

using std::cout; using std::endl;

int main() {
  // Create vertices
  const int N = 6;
  vector<Vertex> v;
  for (int i=0; i<N; i++) {
    Vertex tmp;
    tmp.val=i;
    v.push_back(tmp);
  } 
  
  // Create edges
  vector<Edge> e;
  e.push_back(make_tuple(0,1));
  e.push_back(make_tuple(0,2));
  e.push_back(make_tuple(0,5));
  e.push_back(make_tuple(2,5));
  e.push_back(make_tuple(4,2));
  e.push_back(make_tuple(3,2));

  // Construct undirected graph
  // Graph g(v,e,true);

  // Construct directed graph
  Graph g(v,e,false);

  // Add another node and edge
  g.insert_vx(6);
  g.insert_edge(make_tuple(3,6));
  g.print_map();

  vector<Edge> ex = g.get_edges();
  cout << "(" << get<0>(ex[1]) << "," << get<1>(ex[1]) << ")" << endl;

  Vertex term_node = g.bfs(0,5);
  g.print_path(term_node);
  term_node = g.bfs(3,5);
  g.print_path(term_node);

  vector<int> reached_0 = g.reachable(0);
  cout << "Nodes reachable from 0 are:" << endl;
  for (int i = 0; i < reached_0.size(); i++ ) {
    cout << reached_0[i] << endl;
  }

  vector<int> reached_4 = g.reachable(4);
  cout << "Nodes reachable from 4 are:" << endl;
  for (int i = 0; i < reached_4.size(); i++ ) {
    cout << reached_4[i] << endl;
  }

  return 0;
}

/* OUTPUTS:
Inserting vertex: 6
Inserting Edge: 3,6
Adjacency Map
k: 0, v: [1,2,5,]
k: 1, v: []
k: 2, v: [5,]
k: 3, v: [2,6,]
k: 4, v: [2,]
k: 5, v: []
k: 6, v: []
(0,2)
Found the target node
START --> 0 --> 2 --> 5 --> END
Target node not found
START --> 3 --> END
Nodes reachable from 0 are:
1
2
5
Nodes reachable from 4 are:
2
5
*/