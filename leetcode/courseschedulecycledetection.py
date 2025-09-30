
""""
207. Course Schedule
Medium
Topics
premium lock icon
Companies
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 """




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

def canFinish(numCourses, prerequisites):
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


# Test case
numCourses = 5
prerequisites = [[3,4],[1, 0],[2,1]]  # True
print(canFinish(numCourses, prerequisites))

#
# numCourses = 2
# prerequisites = [[0, 1], [1, 0]]  # False, cycle
# print(canFinish(numCourses, prerequisites))
#
# numCourses = 5
# prerequisites = [[1,0],[2,1],[3,2],[4,3]]  # True, linear
# print(canFinish(numCourses, prerequisites))



#for directed if you also need undirected use parent

# if lst == []:
#     return True
# adj_lst = [[] for i in range(n)]
#
# # adj_dict = {}
# for i in range(len(lst)):
#     adj_lst[lst[i][1]].append(lst[i][0])
#     # adj_lst[lst[i][0]].append(lst[i][1])
#
#     # adj_dict[lst[i][1]] = [lst[i][0]]
# for lst_ in adj_lst:
#     if lst_ == []:
#         lst_.append(None)
# print(adj_lst)
# # print(adj_dict)
# result = []
# # parent = -1
# visited = [False for _ in range(n)]
# stack = [start_vertex]
# if adj_lst[start_vertex] != [None]:
#     visited[start_vertex] = True
# print(visited)
#
# while stack:
#     vertex = stack.pop()
#     result.append(vertex)
#
#     for i in range(len(adj_lst[vertex])):
#         # print(adj_lst[vertex][i], vertex,i,"This")
#         if adj_lst[vertex][i] == None:
#             # print("This has to happen")
#             vertex += 1
#             if vertex == len(adj_lst) or vertex > len(adj_lst):
#                 break
#             stack.append(vertex)
#             continue
#
#         if adj_lst[vertex][i] != None and adj_lst[vertex][i] == adj_lst[vertex]: #self-loop
#             # print(adj_lst[vertex][i])
#             return False
#         if visited[adj_lst[vertex][i]]:
#             print("Visited", adj_lst[vertex][i],vertex,i)
#             return False
#         if not visited[adj_lst[vertex][i]]:
#             value = adj_lst[vertex][i]
#             # print(adj_lst[value],adj_lst[vertex][i],vertex,i)
#             print("again")
#             visited[value] = True
#             stack.append(value)



