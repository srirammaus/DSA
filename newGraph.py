
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v,weight=1):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            # self.adj_matrix[v][u] = weight

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
        print(self.vertex_data[start_vertex], end=' ')
        for i in range(self.size):
            if self.adj_matrix[start_vertex][i] == 1 and not visited[i]:
                self.dfs_recursive(i, visited)
    def dfs(self, vertex):
        visited = [False] * self.size  #seen
        start_vertex = self.vertex_data.index(vertex)
        print(start_vertex)
        # self.dfs_recursive(start_vertex, visited) #D A C B F G E
        self.dfs_while(start_vertex, visited)

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


g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0)  # D - A
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(0, 4)  # A - E
g.add_edge(4, 2)  # E - C
g.add_edge(2, 5)  # C - F
g.add_edge(2, 1)  # C - B
g.add_edge(2, 6)  # C - G
g.add_edge(1, 5)  # B - F

g.print_graph()

print("\nDepth First Search starting from vertex D:")
g.dfs('D')

print("\n bfs")

g.bfs('D')