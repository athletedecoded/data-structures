
# RUN: python py/dijkstra.py

"""
Dijkstra's Algorithm for Non-Negative Weighted Graph using
Min-Heap Priority Queue to solve Single Source Shortest Paths 
"""

from min_heapdict import MinHeapDict
from graph import Vertex, Graph
import math

class PQ(MinHeapDict):
    def __init__(self):
        super().__init__()
    
    def update_dest(self, node, d_est):
        if node < len(self.q):
            # If new distance estimate < curr distance est
            if d_est < self.q[node].val:
                # Update value
                self.q[node].val = d_est
                # Min heapify up to ensure correct heap structure
                self.minify_up(node)

class VDPair:
    """
    {node: min distance estimate pair}
    """
    def __init__(self, node, dest):
        self.key = node
        self.val = dest

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

    def dijkstra(self, s): 
        # Ensure nodes are reset
        self.reset_graph()
        # Init shortest path estimates to infinity
        d = [math.inf for _ in self.v]
        # Init start node
        d[s] = 0
        # Create PQ using MinHeapDict
        Q = PQ()
        # Initialise VD pairs in PQ
        pairs = [VDPair(v.key,d[v.key]) for v in self.v]
        Q.insert(pairs)
        # Iterate
        for _ in range(len(self.v)):
            # Get node with smallest distance estimate
            u = Q.return_min()
            # For nodes adjacent edges
            for v_idx in self.map[u.key]:
                self.relax_edge(d,u.key, v_idx)
                # Update distance estimate 
                Q.update_dest(v_idx, d[v_idx])

        return s, d
    
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
        3: {2:15},
        4: {6:100},
        5: {4:10}}

    print(wg)
    print("----------------------")
    src, wtd_paths = wg.dijkstra(0)
    print(f'The weighted shorted paths from node {src} are: {wtd_paths}')
    wg.print_path(wtd_paths, src)
    print("----------------------")
    src, wtd_paths = wg.dijkstra(3)
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
The weighted shorted paths from node 0 are: [0, 5, 25, 35, 45, 35, 145]
Path from 0 to 1 = 5
(0)---[5]--->(1)
Path from 0 to 2 = 25
(0)---[5]--->(1)---[20]--->(2)
Path from 0 to 3 = 35
(0)---[5]--->(1)---[20]--->(2)---[10]--->(3)
Path from 0 to 4 = 45
(0)---[5]--->(1)---[30]--->(5)---[10]--->(4)
Path from 0 to 5 = 35
(0)---[5]--->(1)---[30]--->(5)
Path from 0 to 6 = 145
(0)---[5]--->(1)---[30]--->(5)---[10]--->(4)---[100]--->(6)
----------------------
The weighted shorted paths from node 3 are: [inf, inf, 15, 0, 65, inf, 165]
Path from 3 to 2 = 15
(3)---[15]--->(2)
Path from 3 to 4 = 65
(3)---[15]--->(2)---[50]--->(4)
Path from 3 to 6 = 165
(3)---[15]--->(2)---[50]--->(4)---[100]--->(6)
"""
