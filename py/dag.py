# RUN: python py/dag.py

"""
Directed Acyclic Graph Implementation & DAG Relaxation

DAG Interface Methods
* insert_vx
* add_edge
* print_map
* bfs
* dfs
* topo_sort
* shortest_path
* reachability
* relaxation
"""

from graph import Vertex, Graph
import math

class DAG(Graph):
    def __init__(self):
        super().__init__()
        self.w = None

    # Recall topo_sort algorthm
    def topo_sort(self, node, topo = []):
        """
        Recursive DFS strategy from source node
        Tracks nodes visited in reverse order
        """
        # Mark node explored
        node.explored = True
        # Get the neighbours of source node
        neighbours = self.map[node.key]
        # For each neighbour
        for idx in neighbours:
            n = self.v[idx]
            if not n.explored:
                # set parent pointer
                n.parent = node
                # recurse along the path of neighbour
                self.topo_sort(n, topo)
        topo.insert(0,node.key)
        return topo
    
    def weight_fxn(self, u, v):
        try:
            w = self.w[u][v]
        except:
            raise Exception("Weight from u to v does not exist")
        return w
    
    def relax_edge(self, d, u, v):
        """
        d: shortest distance estimates for u to v
        """
        # Check violation of triangle inequality 
        if d[v] > d[u] + self.weight_fxn(u,v): 
            d[v] = d[u] + self.weight_fxn(u,v)
            self.v[v].parent = self.v[u]

    def relaxation(self, s): 
        # Ensure nodes are reset
        self.reset_graph()
        # get start node at idx s
        start = self.v[s]
        # generate topo order
        order = self.topo_sort(start)
        # Init shortest path estimates to infinity
        d = [math.inf for _ in self.v]
        # Refresh node state to track parents during relaxation
        self.reset_graph()
        d[s] = 0
        # iterate in topo order
        for u_idx in order:
            # for adjacencies of node
            for v_idx in self.map[u_idx]:
                self.relax_edge(d,u_idx,v_idx)
        
        return s, d
    
    def print_path(self, wtd_paths):
        """
        Given wtd_paths array from DAG relaxation, print path
        taken form source node to all other nodes
        Nodes are indicated in ()
        Edge weights are indicated in []
        """
        # start idx
        u_idx = wtd_paths.index(0)
        # Iterate through array
        for idx in range(len(wtd_paths)):
            # Skip where idx=src or inf
            if wtd_paths[idx] not in [0,math.inf]:
                # Set as the terminating node
                print(f"Path from {u_idx} to {idx} = {wtd_paths[idx]}")
                v = self.v[idx]
                path = [f"({v.key})"]
                while v.parent is not None:
                    path.append(f"---[{self.weight_fxn(v.parent.key,v.key)}]--->")                   
                    path.append(f"({v.parent.key})")
                    v = v.parent
                path.reverse()
                path_str = "".join(path)
                print(path_str)

def main():
    print("----------------------")
    print("Directed Acyclic Graph")
    print("----------------------")

    dag = DAG()

    for i in range(7):
        dag.insert_vx(Vertex(key=i))
    
    edges = [(0,1),(1,5),(5,6),(0,2),(2,3),(2,4),(4,5),(3,6)]
    for edge in edges:
        dag.add_edge(edge, undirected=False)

    # Weights W[i][j] is weight along edge (i,j)
    dag.w = {0:{1:2, 2:5},
        1: {5:-1},
        2: {3:-1,4:1},
        3: {6:4},
        4: {5:2},
        5: {6:3}}

    print(dag)
    print(f'Topo Sort Order: {dag.topo_sort(dag.v[0])}')
    print("----------------------")
    src, wtd_paths = dag.relaxation(0)
    print(f'The weighted shorted paths from node {src} are: {wtd_paths}')
    dag.print_path(wtd_paths)
    print("----------------------")
    src, wtd_paths = dag.relaxation(2)
    print(f'The weighted shorted paths from node {src} are: {wtd_paths}')
    dag.print_path(wtd_paths)

    """
    NOTE: inf weighted path implies it is unreachable
    """

if __name__ == "__main__":
    main()


"""
OUTPUTS
----------------------
Directed Acyclic Graph
----------------------
Vertices: [0, 1, 2, 3, 4, 5, 6], 
Edges: [(0, 1), (1, 5), (5, 6), (0, 2), (2, 3), (2, 4), (4, 5), (3, 6)]
Topo Sort Order: [0, 2, 4, 3, 1, 5, 6]
----------------------
The weighted shorted paths from node 0 are: [0, 2, 5, 4, 6, 1, 4]
Path from 0 to 1 = 2
(0)---[2]--->(1)
Path from 0 to 2 = 5
(0)---[5]--->(2)
Path from 0 to 3 = 4
(0)---[5]--->(2)---[-1]--->(3)
Path from 0 to 4 = 6
(0)---[5]--->(2)---[1]--->(4)
Path from 0 to 5 = 1
(0)---[2]--->(1)---[-1]--->(5)
Path from 0 to 6 = 4
(0)---[2]--->(1)---[-1]--->(5)---[3]--->(6)
----------------------
The weighted shorted paths from node 2 are: [inf, inf, 0, -1, 1, 3, 3]
Path from 2 to 3 = -1
(2)---[-1]--->(3)
Path from 2 to 4 = 1
(2)---[1]--->(4)
Path from 2 to 5 = 3
(2)---[1]--->(4)---[2]--->(5)
Path from 2 to 6 = 3
(2)---[-1]--->(3)---[4]--->(6)
"""
