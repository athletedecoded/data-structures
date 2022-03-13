
# RUN: python py/apsp.py

"""
Johnson's Algorithm for Negative Weighted Graph 
to solve All Pairs Shortest Paths 
"""

from min_heapdict import MinHeapDict
from graph import Vertex, Graph
import math
import copy

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
    
    def save_state(self):
        state = [copy.deepcopy(self.v), copy.deepcopy(self.e), copy.deepcopy(self.w)]
        return state
    
    def reweight(self, wtd_paths):
        for u_idx in self.w:
            for v_idx in self.w[u_idx]:
                self.w[u_idx][v_idx] += (wtd_paths[u_idx] - wtd_paths[v_idx])
        
        # Confirm all weights now non-negative
        print(f"Non-negative weights {self.w}")
        for u,v in self.w.items():
            for wt in v.values():
                if wt < 0:
                    print("Error: found negative weight")

    def johnson(self):
        # Save current G state
        G = self.save_state()
        # Transform G -> Gs
        # Add auxillary super node
        aux_idx = len(self.v)
        self.insert_vx(Vertex(key=aux_idx))
        # Add outgoing edge from aux to all other nodes, set weight = 0
        self.w[aux_idx] = dict()
        for v in self.v:
            if v.key != aux_idx:
                self.add_edge((aux_idx, v.key), undirected=False)
                self.w[aux_idx][v.key] = 0
        # For all u, compute Bellman-Ford, keep track SSSP
        min_cost, min_u, min_v = math.inf, math.inf, math.inf # track SSSP for all u,v
        for u in self.v:
            src, wtd_paths, cycle = self.bellman_ford(u.key)
            if cycle:
                print(cycle)
                return
            else:
                min_cost, min_u, min_v = self.min_SSSP(wtd_paths, min_cost, min_u, min_v, u.key)
        print(f"SSSP by Bellman-Ford is {min_u} --> {min_v}, cost = {min_cost}")       
        # Restore state G
        self.v, self.e, self.w = G
        # Construct G'
        # Reweight each edge: w'(u,v) = w(u, v) + d[u] - d[v]
        self.reweight(wtd_paths)
        # V x Dijkstra
        min_cost, min_u, min_v = math.inf, math.inf, math.inf # track SSSP for all u,v
        for u in self.v:
            src, wtd_paths = self.dijkstra(u.key)
            min_cost, min_u, min_v = self.min_SSSP(wtd_paths, min_cost, min_u, min_v, u.key)
        print(f"SSSP by Johnson + Dijkstra is {min_u} --> {min_v}, cost = {min_cost}")

        return min_u

    def min_SSSP(self, wtd_paths, min_cost, min_u, min_v, curr_u):
        for idx in range(len(wtd_paths)):
            if idx == curr_u:
                continue
            if wtd_paths[idx] < min_cost:
                min_cost = wtd_paths[idx]
                min_u = curr_u
                min_v = idx
        return min_cost, min_u, min_v


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

def neg_cycle():
    wg = WtdGraph()

    for i in range(7):
        wg.insert_vx(Vertex(key=i))
    
    edges = [(0,1),(1,2),(2,3),(3,2),(1,5),(5,4),(2,4),(4,6)]
    for edge in edges:
        wg.add_edge(edge, undirected=False)

    # Demo Negative Cycle
    # Weights W[i][j] is weight along edge (i,j)
    wg.w = {0:{1:5},
        1: {2:20, 5:30},
        2: {3:10,4:50},
        3: {2:-15},
        4: {6:100},
        5: {4:-10}}
    
    src = wg.johnson()

def apsp():
    wg = WtdGraph()

    for i in range(7):
        wg.insert_vx(Vertex(key=i))
    
    edges = [(0,1),(1,2),(2,3),(3,2),(1,5),(5,4),(2,4),(4,6)]
    for edge in edges:
        wg.add_edge(edge, undirected=False)

    # Weights W[i][j] is weight along edge (i,j)
    wg.w = {0:{1:5},
        1: {2:20, 5:30},
        2: {3:-10,4:50},
        3: {2:15},
        4: {6:100},
        5: {4:-10}}

    src = wg.johnson()
    src, wtd_paths = wg.dijkstra(src)
    wg.print_path(wtd_paths, src)



def main():
    print("----------------------")
    print("Demo Negative Cycle")
    neg_cycle()
    print("----------------------")
    print("Demo Johnson's APSP")
    apsp()

if __name__ == "__main__":
    main()


"""
OUTPUTS
----------------------
Demo Negative Cycle
Negative weight cycle found from 2 to 3
----------------------
Demo Johnson's APSP
SSSP by Bellman-Ford is 2 --> 3, cost = -10
Non-negative weights {0: {1: 5}, 1: {2: 20, 5: 30}, 2: {3: 0, 4: 60}, 3: {2: 5}, 4: {6: 90}, 5: {4: 0}}
SSSP by Johnson + Dijkstra is 2 --> 3, cost = 0
Path from 2 to 3 = 0
(2)---[0]--->(3)
Path from 2 to 4 = 60
(2)---[60]--->(4)
Path from 2 to 6 = 150
(2)---[60]--->(4)---[90]--->(6)
"""
