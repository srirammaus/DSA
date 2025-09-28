
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v,weight=1):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(lambda x: str(x) if x is not None else '0', row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
    def dfs_recursive(self, start_vertex, visited):
        visited[start_vertex] = True
        # print(self.vertex_data[start_vertex], end=' ')
        for i in range(self.size):
            if self.adj_matrix[start_vertex][i] == 1 and not visited[i]:
                # print("Im the reason before C 0 2")
                self.dfs_recursive(i, visited)
            # elif visited[i]:
            #     print(self.vertex_data[start_vertex],i,start_vertex,"visited fake")
            # else:
            #     print(self.vertex_data[start_vertex], i, start_vertex,"Nothing here")
    def dfs(self, vertex):
        visited = [False] * self.size  #seen
        start_vertex = self.vertex_data.index(vertex)
        print(start_vertex)
        self.dfs_recursive(start_vertex, visited) #D A C B F G E
        # self.dfs_while(start_vertex, visited)

    # dfs_while produces different answer from resursive , thats nature not a problem
    def dfs_while(self,vertex, visited):
        visited[vertex] = True
        result = []
        stack = [vertex]

        while stack:
            vertex = stack.pop()
            result.append(self.vertex_data[vertex])
            for i in range(self.size):
                if self.adj_matrix[vertex][i] == 1 and not visited[i]:
                    visited[i] = True
                    stack.append(i)
        print(result)

    def bfs(self,vertex):
        visited = [False] * self.size
        start_vertex = self.vertex_data.index(vertex)
        queue = [start_vertex]
        visited[queue[0]] = True
        result = []
        while queue:
            vertex = queue.pop(0)
            result.append(self.vertex_data[vertex])
            for i in range(self.size):
                if self.adj_matrix[vertex][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)

        print(result)
    def isCyclic(self):
        visited = [False] * self.size
        for i in range(self.size):
            if not visited[i]:
                if self.dfs_cycle(i, visited, -1):
                    return True
        return False
    def dfs_cycle(self,v, visited, parent):
        visited[v] = True
        for i in range(self.size):
            if self.adj_matrix[v][i] == 1:
                # print(parent,v,i,self.vertex_data[parent])
                if not visited[i]:
                    # print("This happened finally 1")
                    if self.dfs_cycle(i, visited, v):
                        return True
                elif parent != i:
                    # print("This happened finally 2",parent,i)
                    return True

        return False


g = Graph(3)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
# g.add_vertex_data(3, 'D')
# g.add_vertex_data(4, 'E')
# g.add_vertex_data(5, 'F')
# g.add_vertex_data(6, 'G')

g.add_edge(0, 1)  # D - A
g.add_edge(1, 2)  # A - C
g.add_edge(2, 0)
# g.add_edge(0, 3)  # A - D
# g.add_edge(0, 4)  # A - E
# g.add_edge(4, 2)  # E - C
# g.add_edge(2, 5)  # C - F
# g.add_edge(2, 1)  # C - B
# g.add_edge(2, 6)  # C - G
# g.add_edge(1, 5)  # B - F

g.print_graph()

# print("\nDepth First Search starting from vertex D:")
# g.dfs('A')

# print("\n bfs")

# g.bfs('A')

print("  ")
print("is cyclic")

print(g.isCyclic())


"""
use this example to understand cyclic in undirected
the below first example is not a cyclic but this makes sense why parent needed
we make A as visted true before loop start , the A's 0 index is 0(as you see below matrix), then while seeing the the == 1 is 1th index and that is not visted 
so recursion happen going B . B's 0th index is 1 (see below matrix) , from this what you know is that you can
skip the visited by using "not visited" . so here were if you use this regular function finding cyclic put you in confused 
state , becuase B's 0th index 1 shows visited , you dont take this final and say this cyclic becuase this is undirected both ways are
there A-B, B-A , so by checking this visited just blind without know who is the parent you will get wrong result 

0 1 1
1 0 0
1 0 0

g = Graph(3)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')

g.add_edge(0, 1)  # A-B
g.add_edge(0, 2)  # A -C


def dfs_recursive(self, start_vertex, visited):
    visited[start_vertex] = True
    # print(self.vertex_data[start_vertex], end=' ')
    for i in range(self.size):
        if self.adj_matrix[start_vertex][i] == 1 and not visited[i]:
            # print("Im the reason before C 0 2")
            self.dfs_recursive(i, visited)
        elif visited[i]:
            print(self.vertex_data[start_vertex],i,start_vertex,"visited fake")
        else:
            print(self.vertex_data[start_vertex], i, start_vertex,"Nothing here")

"""