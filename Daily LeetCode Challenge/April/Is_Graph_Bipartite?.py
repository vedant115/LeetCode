# LeetCode 785. Is Graph Bipartite?

"""
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

 

Example 1:


Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
"""

class Solution:

    def isBipartite(self, graph: list[list[int]]) -> bool:
	
        vis = [False for n in range(0, len(graph))]
        
        while sum(vis) != len(graph): # Since graph isn't required to be connected this process needs to be repeated

            ind = vis.index(False) # Find the first entry in the visited list that is false
            vis[ind] = True
            grp = {ind:True} # initialize first node as part of group 1
            q = [ind] # Add current index to queue
            
            while q: # Go to each node in the graph
                u = q.pop(0)

                for v in graph[u]: # Go to each vertice connected to the current node

                    if vis[v] == True: #  If visited check that it is in the opposite group of the current node
                        if grp[u] == grp[v]:
                            return False # If a single edge does not lead to a group change return false

                    else: # If not visited put v in opposite group of u, set to visited, and append to q
                        vis[v] = True
                        grp[v] = not grp[u]
                        q.append(v)
        
        return True
