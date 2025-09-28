"""
Check a path is existing or not in grapg leetcode 1971

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.



Example 1:


Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
Example 2:


Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
"""

# class Graph:
#     def __init__(self,size,source,destination):
#         self.adj_matrix = [[None]* size for _ in range(size)]
#         self.size = size
#         # self.result = []
#         # self.vertices = [" " * self.size ]  neeeed if there is alphabets
#         self.result = 0
#         self.source = source
#         self.destination = destination
#
#     def addEdge(self,u,v): #undirected
#         self.adj_matrix[u][v] = 1
#         self.adj_matrix[v][u] = 1
#
#     def dfs_recursive(self,v,visited):
#         visited[v] = True
#         # self.result.append(v)
#
#         if v == self.source or v == self.destination :
#             self.result += 1
#         if self.result == 2:
#             return True
#
#         for i in range(self.size):
#             if self.adj_matrix[v][i] and not visited[i]:
#                 if self.dfs_recursive(i,visited):
#                     return True
#         return False
#     def dfs(self,source_vertex):
#         visited = [False] * self.size
#         return self.dfs_recursive(source_vertex,visited)
#     def print_graph(self):
#         print("Adjacency Matrix:")
#         for row in self.adj_matrix:
#             print(' '.join(map(lambda x: str(x) if x is not None else '0', row)))
#         print("-------")

# n = 3
# edges = [[0,1],[1,2],[2,0]]
# source = 0
# destination = 2
#
#
#
# graph = Graph(n,source,destination)
#
# # add edges
# for i in range(len(edges)):
#     graph.addEdge(edges[i][0],edges[i][1])
#
# graph.print_graph()
#
# print(graph.dfs(0))
# print(graph.result)



class Graphlist:
    def validPath(self,size,edges,source,destination) ->bool:
        # building adjecny list , becuse matrix cant handle too much memmroy
        self.adj_list = [[] for _ in range(n)]
        for u, v in edges:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
        print(self.adj_list)
        self.size = size
        self.source = source
        self.destination = destination
        self.result = 0

        if  source == destination:
            return True
        self.queue = [source]
        self.visited = [False] * n
        self.visited[source] = True
        while self.queue:

            # print(self.queue)
            v = self.queue.pop(0)
            # print(v)
            if v == self.source or v == self.destination :
                self.result += 1
            if self.result == 2:
                return True
            for i in range(len(self.adj_list[v])):
                if not self.visited[self.adj_list[v][i]]:

                    self.visited[self.adj_list[v][i]] = True
                    self.queue.append(self.adj_list[v][i])
            # print(self.queue)
        return False
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2





graph = Graphlist()

print(graph.validPath(n,edges,source,destination))

# def checkPathExists(self,source_vertex,destination_vertex):
#     # print(self.result)
#     if(source_vertex in self.result and destination_vertex in self.result):
#         return True
#     return False

# print(graph.checkPathExists(source,destination))
