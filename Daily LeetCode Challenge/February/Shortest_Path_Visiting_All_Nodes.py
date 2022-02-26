# LeetCode 847

"""
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

Example 1:

Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
"""


def shortestPathLength(self, graph: List[List[int]]) -> int:
	length = len(graph)
	result = 0
	visited_node = []
	queue = []  
  
	for i in range(length):
		visited_node.append(set([1<<i]))
		queue.append([i,1<<i])
    
	while queue:
		result = result + 1
		new_queue = []
           
		for node, value in queue:
			for neigbour_node in graph[node]:
				mid_node = (1<<neigbour_node)|value
				if mid_node not in visited_node[neigbour_node]:
					if mid_node+1 == 1<<length:
						return result
          
					visited_node[neigbour_node].add(mid_node)
					new_queue.append([neigbour_node, mid_node])
          
		queue = new_queue
    
	return 0
