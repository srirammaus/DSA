
def dfs_util(adjacency_list, vertex, visited, recStack):
    visited[vertex] = True
    recStack[vertex] = True
    print(recStack,vertex)
    for neighbor in adjacency_list[vertex]:
        if not visited[neighbor]:
            if not dfs_util(adjacency_list, neighbor, visited, recStack):
                return False
        elif recStack[neighbor]:  # cycle detected
            return False

    recStack[vertex] = False  # remove from recursion stack
    return True

def canFinishdisconnected(numCourses, prerequisites):  #for disconnected graph
    # Build adjacency list
    adj_lst = {i: [] for i in range(numCourses)}
    for dest, src in prerequisites:
        adj_lst[src].append(dest)

    visited = [False] * numCourses
    recStack = [False] * numCourses

    for vertex in range(numCourses):
        if not visited[vertex]:
            if not dfs_util(adj_lst, vertex, visited, recStack):
                return False

    return True

def canFinishconnected(numCourses, prerequisites ,vertex = 0):  #for connected graph
    # Build adjacency list
    adj_lst = {i: [] for i in range(numCourses)}
    for dest, src in prerequisites:
        adj_lst[src].append(dest)

    visited = [False] * numCourses
    recStack = [False] * numCourses

    if not dfs_util(adj_lst, vertex, visited, recStack):
        return False

    return True


# Test case
numCourses = 5
prerequisites = [[3,4],[1, 0],[2,1]]  # True
print(canFinishdisconnected(numCourses, prerequisites))


"""
This below works for connected and they should be start from vertex 0 , i means the here in this method list should be empty that kind it need"""
def adjListCycledetection(n,start_vertex,lst):
    result = []
    parent = -1
    visited = [False for _ in range(n)]
    stack = [(start_vertex,parent)]
    visited[start_vertex] = True
    while stack:
        vertex,parent = stack.pop()
        result.append(vertex)
        for i in range(len(lst[vertex])):
            if not visited[lst[vertex][i]]:
                print(lst[vertex][i],vertex,i)
                visited[lst[vertex][i]] = True
                stack.append( (lst[vertex][i],vertex))
            #parent check need only if the graph is undirected
            elif parent != lst[vertex][i]:
                print(lst[vertex][i], vertex, i,parent)
                return True #yes this is cylic

    return False

#adjacent list always use dict , using list might sometimes not work as intented , it has to loop uncessarly so use dict
#n should be given correctly during adjancy list, sometimes [[1,2],[0,3]]  if you put n as 2 it wont work as you know adj_list work
#with values , so as of here , during this process it might get the value 3 and then it looks for index 3 but you max is 2 , so it throws error


# def adjacency_list_dictionary(V, edges):
#     adjacency_list = {}
#
#     # Add vertices to the dictionary
#     for i in range(V):
#         adjacency_list[i] = []
#
#     # Add edges to the dictionary
#     for edge in edges:
#         vertex1, vertex2 = edge
#         adjacency_list[vertex1].append(vertex2)
#
#     return adjacency_list