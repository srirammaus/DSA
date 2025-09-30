def dfs_util(adjacency_list, vertex, visited):
    visited[vertex] = True
    print(vertex, end=" ")
    for neighbor in adjacency_list[vertex]:
        # if visited[neighbor]:
        #     print(neighbor, "He is visited")
        if not visited[neighbor]:
            dfs_util(adjacency_list, neighbor, visited)

def dfs_disconnected(adjacency_list,vertex,visited):
    # visited = set()
    for vertex in adjacency_list:

        if not visited[vertex]:
            dfs_util(adjacency_list, vertex, visited)



#



# Example usage
V = 6
edges = [[0, 1], [1, 2], [2, 3],[3,1]]
adjacency_list = {i: [] for i in range(V)}
for u, v in edges:
    adjacency_list[u].append(v)
    # adjacency_list[v].append(u)  # If undirected

print(adjacency_list)

visited = [False] * V
# dfs_disconnected(adjacency_list,0,visited) #if you need all eveything , eventhough they are disconnected use this or directly use below
dfs_util(adjacency_list,0,visited)