# Clone Graph

# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
# code
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        nodes = []
        seen = [0]* 101
        nodes.append(0)
        for i in range(100):
            nodes.append(Node(i+1))
        def dfs(n,cp):
            if seen[n.val] == 1:
                return
            seen[n.val] = 1
            if n.neighbors == None:
                cp.neighbors = None
                return

            for i in n.neighbors:
                cp.neighbors.append(nodes[i.val])
                dfs(i,nodes[i.val])
        dfs(node,nodes[node.val])

        return nodes[node.val]




        