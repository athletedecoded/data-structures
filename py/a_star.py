
# RUN: python py/a_star.py

"""
A* Search Algorithm for Non-Negative Weighted Graph
Searches for path between src and target nodes

A* vs Dijkstra:
* Dijkstra selects node with smallest weighted distance estimate
* A* selects node with smallest cost function, f(n)
* Dijkstra is guaranteed to find optimal path, A* is not
* A* efficiency typically better Dijkstra
* Dijkstra is equivalent to h(n) = 0

f(n) = g(n) + h(n)
* g(n) = cost to reach node from source, ie. d_est from src to node
* h(n) = heuristic cost of reaching target from node

In coordinate based graphs, can use Euclidean or Mannhattan 
distance to estimate the heuristic, h(n). Here, we are in non-coord space
and perform a level-order scan using BFS. The heuristic is then 
estimated as the level difference between the node and target.
"""

from min_heapdict import MinHeapDict
from dijkstra import WtdGraph
import math

class PQ(MinHeapDict):
    def __init__(self):
        super().__init__()
    
    def update_cost(self, node):
        if node.key < len(self.q):
            # If new cost estimate < curr cost est
            if node.f < self.q[node.key].val:
                # Update value
                self.q[node.key].val = node.f
                # Min heapify up to ensure correct heap structure
                self.minify_up(node.key)

class Vertex():
    def __init__(self, key, parent=None, explored=False):
        self.key = key
        self.parent = parent
        self.explored = explored
        self.lvl = None
        self.g = math.inf # cost to reach node from src
        self.h = 0 # heuristic cost from this node to goal
        self.f = math.inf

class VCPair:
    """
    Vertex-Cost pair {node: f(n)}
    """
    def __init__(self, node, f):
        self.key = node
        self.val = f

class AStarGraph:
    def __init__(self):
        self.v = []
        self.e = []
        self.map = None
        self.w = None
    
    def __str__(self):
        return (f"Vertices: {[v.key for v in self.v]}, \nEdges: {self.e}")
    
    def insert_vx(self, vx):
        # Ensure unique node val
        keys = [v.key for v in self.v]
        if vx.key in keys:
            print("This vertex already exists")
        else:
            # Add node
            self.v.append(vx)
        # Update map
        self.map = self.graph_map()
    
    def add_edge(self, edge, undirected = True):
        if edge in self.e:
            print("This edge already exists")
        else:
            # Add edge
            self.e.append(edge)
            if undirected:
                self.e.append((edge[1],edge[0]))
        # Update map
        self.map = self.graph_map()
    
    def graph_map(self):
        map = dict()
        # For all nodes
        for v in self.v:
            # Create map idx == node.key
            map[v.key] = set()
            # For all edges
            for e in self.e:
                # if idx is the start of an edge
                if e[0] == v.key:
                    # add the neighbour to its set
                    map[v.key].add(e[1])
        return map

    def print_map(self):
        """
        Prints adjacency map
        """
        print(f"Graph Map: {self.map}")

    def reset_graph(self):
        """
        Resets node states
        """
        for v in self.v:
            v.parent = None
            v.explored = False
 
    def weight_fxn(self, u, v):
        try:
            w = self.w[u][v]
        except:
            raise Exception(f"Weight from {u} to {v} does not exist")
        return w
    
    def relax_edge(self, u, v):
        """
        input: nodes u, v
        """
        # Check violation of triangle inequality 
        if v.g > u.g + self.weight_fxn(u.key,v.key): 
            # update d_est to v
            v.g = u.g + self.weight_fxn(u.key,v.key)
            # update cost fxn, v.f
            v.f = v.g + v.h
            # set parent pointer v --> u
            self.v[v.key].parent = self.v[u.key]
    
    def level_order(self, src_node):
        """
        Determine level order of graph using BFS search strategy
        """
        # Initialise frontier queue with src node
        frontier = [src_node]
        lvl = 0
        src_node.lvl = lvl
        # While frontier is not empty
        while frontier:
            # Get next idx from the queue frontier and get node
            nxt_idx = frontier.pop(0).key
            node = self.v[nxt_idx]
            # Mark explored
            node.explored = True
            # Add node's neighbours to frontier, if not explored yet
            neighbours = self.map[node.key]
            for idx in neighbours:
                n = self.v[idx]
                if not n.explored:
                    n.parent = node
                    n.lvl = n.parent.lvl + 1
                    frontier.append(n)
        # If target node not found, return none
        return [(x.key, x.lvl) for x in self.v] 

    def heuristic_estimate(self, target):
        # Init heuristic values: target.lvl - node.lvl
        for node in self.v:
            node.h = abs(target.lvl - node.lvl)
        return [(x.key, x.h) for x in self.v] 

    def a_star(self, src, target): 
        # Ensure nodes are reset
        self.reset_graph()
        # Level order scan to update node levels
        self.level_order(src)
        # Init heuristic values: target.lvl - node.lvl
        self.heuristic_estimate(target)
        # Init src node dist
        src.g = 0
        src.f = src.g + src.h
        # Create frontier PQ using MinHeapDict
        Q = PQ()
        # Initialise VD pairs in PQ
        pairs = [VCPair(v.key,v.f) for v in self.v]
        Q.insert(pairs)
        # Iterate
        for _ in range(len(self.v)):
            # Get node with smallest cost estimate
            u = Q.return_min()
            # For nodes adjacent edges
            for v_idx in self.map[u.key]:
                # Calculate distance est from src to node
                self.relax_edge(self.v[u.key], self.v[v_idx])
                # Update cost estimate 
                Q.update_cost(self.v[v_idx])

        path, path_str = self.print_path(target)
        costs = list(zip([x.f for x in self.v],[x.g for x in self.v]))
        print(f"A* found a path from {src.key} to {target.key}: {path_str}")
        return costs
        
    def print_path(self, term_node):
        """
        Given the terminating node and self.v has set of parent pointers
        Return path, path_str
        """
        path = [str(term_node.key)]
        while term_node.parent is not None:
            path.append(str(term_node.parent.key))
            term_node = term_node.parent
        path.reverse()
        path_str = "-->".join(path)
        return path, path_str


def main():

    asg = AStarGraph()
    wg = WtdGraph()

    for i in range(7):
        asg.insert_vx(Vertex(key=i))
        wg.insert_vx(Vertex(key=i))
    
    edges = [(0,1),(1,2),(2,3),(1,5),(5,4),(2,4),(4,6)]
    for edge in edges:
        asg.add_edge(edge, undirected=False)
        wg.add_edge(edge, undirected=False)

    # Weights W[i][j] is weight along edge (i,j)
    weights = {0:{1:5},
        1: {2:20, 5:30},
        2: {3:10,4:50},
        4: {6:25},
        5: {4:10}}
    
    asg.w = weights
    wg.w = weights

    for i in range(7):
        asg.a_star(asg.v[0], asg.v[i])
    print("----------------------")
    print("Compare with Dijkstra")
    src, wtd_paths = wg.dijkstra(0)
    print(f'The weighted shorted paths from node {src} are: {wtd_paths}')
    wg.print_path(wtd_paths, src)

if __name__ == "__main__":
    main()


"""
OUTPUTS
A* found a path from 0 to 0: 0
A* found a path from 0 to 1: 0-->1
A* found a path from 0 to 2: 0-->1-->2
A* found a path from 0 to 3: 0-->1-->2-->3
A* found a path from 0 to 4: 0-->1-->5-->4
A* found a path from 0 to 5: 0-->1-->5
A* found a path from 0 to 6: 0-->1-->5-->4-->6
----------------------
Compare with Dijkstra
The weighted shorted paths from node 0 are: [0, 5, 25, 35, 45, 35, 70]
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
Path from 0 to 6 = 70
(0)---[5]--->(1)---[30]--->(5)---[10]--->(4)---[25]--->(6)
"""
