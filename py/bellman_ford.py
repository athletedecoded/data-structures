
# RUN: python py/bellman_ford.py

"""
Bellman-Ford Algorithm for Negative Weighted Graph 
to solve Single Source Shortest Paths 
"""

from graph import Vertex, Graph
import math

class WtdGraph(Graph):
    def __init__(self):
        super().__init__()
        self.w = None
   
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

    def bellman_ford(self, s): 
        # Ensure nodes are reset
        self.reset_graph()
        # Init shortest path estimates to infinity
        d = [math.inf for _ in self.v]
        # Init start node
        d[s] = 0
        # Loop for |V|-1 rounds
        V = len(self.v)
        for k in range(V-1):
            # Over each node, u
            for u in self.v:
                # For every adjacent node, v
                for v in self.map[u.key]:
                    self.relax_edge(d,u.key, v)
        # After termination, check if any edges can be relaxed further/violate
        # triangle inequality. If so, there must be a negative weight cycle
        cycle = None
        for u in self.v:
            # For every adjacent node, v
            for v in self.map[u.key]:
                if d[v] > d[u.key] + self.weight_fxn(u.key,v):
                    cycle = f"Negative weight cycle found from {u.key} to {v}"
        return s, d, cycle
    
    def print_path(self, wtd_paths, s):
        """
        Given wtd_paths array print path taken form source node to all other nodes
        Nodes are indicated in ()
        Edge weights are indicated in []
        """
        # Iterate through array
        for idx in range(len(wtd_paths)):
            # Skip where idx=src or inf
            if not ((idx==s) or (wtd_paths[idx]== math.inf)):
                # Set as the terminating node
                print(f"Path from {s} to {idx} = {wtd_paths[idx]}")
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
    wg = WtdGraph()

    for i in range(7):
        wg.insert_vx(Vertex(key=i))
    
    edges = [(0,1),(1,2),(2,3),(3,2),(1,5),(5,4),(2,4),(4,6)]
    for edge in edges:
        wg.add_edge(edge, undirected=False)

    # Weights W[i][j] is weight along edge (i,j)
    wg.w = {0:{1:5},
        1: {2:20, 5:30},
        2: {3:10,4:50},
        3: {2:-15},
        4: {6:100},
        5: {4:-10}}

    print(wg)
    print("----------------------")
    src, wtd_paths, cycle = wg.bellman_ford(0)
    if cycle:
        print(cycle)
    else:
        print(f'The weighted shorted paths from node {src} are: {wtd_paths}')
        wg.print_path(wtd_paths, src)
    print("----------------------")
    src, wtd_paths, cycle = wg.bellman_ford(5)
    if cycle:
        print(cycle)
    else:
        print(f'The weighted shorted paths from node {src} are: {wtd_paths}')
        wg.print_path(wtd_paths, src)
    print("----------------------")

    """
    NOTE: inf weighted path implies it is unreachable
    """

if __name__ == "__main__":
    main()


"""
OUTPUTS
Vertices: [0, 1, 2, 3, 4, 5, 6], 
Edges: [(0, 1), (1, 2), (2, 3), (3, 2), (1, 5), (5, 4), (2, 4), (4, 6)]
----------------------
Negative weight cycle found from 2 to 3
----------------------
The weighted shorted paths from node 5 are: [inf, inf, inf, inf, -10, 0, 90]
Path from 5 to 4 = -10
(5)---[-10]--->(4)
Path from 5 to 6 = 90
(5)---[-10]--->(4)---[100]--->(6)
"""
