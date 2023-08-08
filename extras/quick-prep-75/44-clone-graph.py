
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # keep track of already visited neighbors
        cloner_hash = {}
        def dfs(graph):
            if graph in cloner_hash:
                return cloner_hash[graph]
            copy = Node(graph.val)
            cloner_hash[graph] = copy
            for neighbor_node in graph.neighbors:
                copy.neighbors.append(dfs(neighbor_node))
            return copy
        # if there is no node 
        return dfs(node) if node else None
            