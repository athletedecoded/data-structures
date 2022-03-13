# RUN: python dsa/py/graph.py

"""
Unweighted Graph Implementation for directed or undirected graphs

Graph Interface Methods
* insert_vx
* add_edge
* print_map
* bfs
* dfs
* topo_sort
* shortest_path
* reachability
"""
class Vertex():
    def __init__(self, key, parent=None, explored=False):
        self.key = key
        self.parent = parent
        self.explored = explored

class Graph:
    def __init__(self):
        self.v = []
        self.e = []
        self.map = None
    
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
    
    def bfs(self, src_node, trgt_node):
        """
        Breadth first search strategy from source node to target node
        """
        # Initialise frontier queue with src node
        frontier = [src_node]
        # While frontier is not empty
        while frontier:
            # Get next idx from the queue frontier and get node
            nxt_idx = frontier.pop(0).key
            node = self.v[nxt_idx]
            # If this is target node, return node
            if node == trgt_node:
                return node
            # Mark explored
            node.explored = True
            # Add node's neighbours to frontier, if not explored yet
            neighbours = self.map[node.key]
            for idx in neighbours:
                n = self.v[idx]
                if not n.explored:
                    n.parent = node
                    frontier.append(n)
        # If target node not found, return none
        return None
    
    def reset_graph(self):
        """
        Resets node states
        """
        for v in self.v:
            v.parent = None
            v.explored = False
   
    def dfs(self, node):
        """
        Recursive DFS strategy from source node to target node
        Recall: recursive calls act like a stack
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
                self.dfs(n)
    
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


    def shortest_path(self, src_node, trgt_node):
        """
        Determines shortest path from src node to trgt node usign BFS
        Displays path if it exists
        """
        term_node = self.bfs(src_node, trgt_node)

        if term_node is None:
            print(f"No path between {src_node.key} and {trgt_node.key}")
            return

        path, path_str = self.print_path(term_node)
        # Number of edges = number of nodes - 1
        print(f"Shortest path from {src_node.key} to {trgt_node.key}: {len(path) - 1} edges")
        print(path_str)

        # reset nodes
        self.reset_graph()
    
    def reachability(self,node):
        """
        Uses DFS to determine set of nodes reachable from given node
        """
        # Ensure nodes are reset
        self.reset_graph()
        # Call dfs
        self.dfs(node)
        # Check which nodes have been explored
        explored = set()
        for v in self.v:
            if v.explored:
                explored.add(v.key)
        # Ignore initial node
        explored -= {node.key}
        if explored:
            print(f"From vertex {node.key} we can reach vertices {explored}")
        else:
            print(f"Vertex {node.key} cannot reach any other vertices")

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

def undirected():
    print("----------------------")
    print("Undirected Graph")
    print("----------------------")
    ug = Graph()

    for i in range(7):
        ug.insert_vx(Vertex(key=i))

    edges = [(0,1), (0,2), (0,5), (2,5), (4,2), (3,2), (3,6)]
    for edge in edges:
        ug.add_edge(edge, undirected=True)
    
    print(ug)
    ug.print_map()
    ug.shortest_path(ug.v[0], ug.v[6])
    ug.reachability(ug.v[4])

def directed():
    print("----------------------")
    print("Directed Graph")
    print("----------------------")

    dg = Graph()

    for i in range(7):
        dg.insert_vx(Vertex(key=i))

    edges = [(0,1), (0,5), (0,2), (2,5), (4,2), (3,2), (3,6)]
    for edge in edges:
        dg.add_edge(edge, undirected=False)
    
    print(dg)
    dg.print_map()
    dg.shortest_path(dg.v[1], dg.v[5])
    dg.reachability(dg.v[4])

def dag():
    print("----------------------")
    print("Directed Acyclic Graph")
    print("----------------------")

    dag = Graph()

    for i in range(5):
        dag.insert_vx(Vertex(key=i))
    
    edges = [(0,1), (1,3), (0,2), (2,3), (3,4)]
    for edge in edges:
        dag.add_edge(edge, undirected=False)

    print(dag)
    print(f'Topo Sort Order: {dag.topo_sort(dag.v[0])}')


if __name__ == "__main__":
    undirected()
    directed()
    dag()


"""
OUTPUT
----------------------
Undirected Graph
----------------------
Vertices: [0, 1, 2, 3, 4, 5, 6], 
Edges: [(0, 1), (1, 0), (0, 2), (2, 0), (0, 5), (5, 0), (2, 5), (5, 2), (4, 2), (2, 4), (3, 2), (2, 3), (3, 6), (6, 3)]
Graph Map: {0: {1, 2, 5}, 1: {0}, 2: {0, 3, 4, 5}, 3: {2, 6}, 4: {2}, 5: {0, 2}, 6: {3}}
Shortest path from 0 to 6: 3 edges
0-->2-->3-->6
From vertex 4 we can reach vertices {0, 1, 2, 3, 5, 6}
----------------------
Directed Graph
----------------------
Vertices: [0, 1, 2, 3, 4, 5, 6], 
Edges: [(0, 1), (0, 5), (0, 2), (2, 5), (4, 2), (3, 2), (3, 6)]
Graph Map: {0: {1, 2, 5}, 1: set(), 2: {5}, 3: {2, 6}, 4: {2}, 5: set(), 6: set()}
No path between 1 and 5
From vertex 4 we can reach vertices {2, 5}
----------------------
Directed Acyclic Graph
----------------------
Vertices: [0, 1, 2, 3, 4], 
Edges: [(0, 1), (1, 3), (0, 2), (2, 3), (3, 4)]
Topo Sort Order: [0, 2, 1, 3, 4]
"""