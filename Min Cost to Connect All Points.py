# Min Cost to Connect All Points
# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

class Graph:
    # Constructor to initialize the graph with 'vertices' number of vertices
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # Function to add an edge to the graph between vertices 'u' and 'v' with weight 'w'
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Helper function to find the parent of a node 'i'
    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    # Helper function to perform a union operation between sets of 'u' and 'v'
    def union(self, parent, rank, u, v):
        u_set = self.find_parent(parent, u)
        v_set = self.find_parent(parent, v)

        if rank[u_set] < rank[v_set]:
            parent[u_set] = v_set
        elif rank[u_set] > rank[v_set]:
            parent[v_set] = u_set
        else:
            parent[v_set] = u_set
            rank[u_set] += 1

    # Kruskal's algorithm to find the minimum spanning tree
    def kruskal(self):
        result = []
        i, e = 0, 0

        # Sort the edges based on their weights
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Initialize parent and rank arrays
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Initialize a graph with the number of vertices
        g = Graph(len(points))

        # Populate the graph with edges and weights
        for i in range(len(points)):
            p1 = points[i]
            for j in range(i + 1, len(points)):
                p2 = points[j]
                d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                g.add_edge(i, j, d)

        # Find the minimum spanning tree using Kruskal's algorithm
        mst = g.kruskal()

        # Calculate the total cost of the MST
        total_cost = sum(edge[2] for edge in mst)

        return total_cost