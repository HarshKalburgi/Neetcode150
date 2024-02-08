# Redundant Connection

# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1) # rank measure size of graph

        def find(v): # finds the parent of v
            p = parent[v]
            while p != parent[p]:
                parent[p] = parent[parent[p]] # path compression
                p = parent[p]
            return p

        def union(v1, v2):
            p1, p2 = find(v1), find(v2)

            if p1 == p2: return False
            
            # p1 should be the larger disjoint graph (e.g. tree)
            if rank[p1] < rank[p2]: p1, p2 = p2, p1

            rank[p1] += rank[p2]
            parent[p2] = p1

            return True
        
        # since we don't create the full graph, but rather union iteratively
        # the redundant connection will be the first and last in edges
        for a, b in edges:
            if not union(a, b):
                return (a, b)
