import random

class graph:
    def __init__(self, number_of_vertex) -> None:
        self.number_of_vertex = number_of_vertex
        self.adjacency_list = self._start_list()

    def _start_list(self):
        adjacency_list = {}
        for i in range(self.number_of_vertex):
            adjacency_list[i] = []
        return adjacency_list
        # this for generate a list of lists going from 0 to 99 empty

    def generate_edges(self):
        for i in range(self.number_of_vertex):
            # this for generate a random number to be the degree of the vertex
            random_vertex_degree = random.randrange(0, self.number_of_vertex - 1)
            while len(self.adjacency_list[i]) < random_vertex_degree:
                # this is a loop inside the vertex i to generate the vertices adjacent to i
                random_vertex = random.randrange(0, self.number_of_vertex)

                if random_vertex not in self.adjacency_list[i]:
                    self.insertion_sort(self.adjacency_list[i], random_vertex)
                    self.insertion_sort(self.adjacency_list[random_vertex], i)

    def insertion_sort(self, list, vertex):
        if vertex not in list:
            if not list:
                list.append(vertex)
            else:
                for i in range(len(list)):
                    if vertex < list[i]:
                        list.insert(i, vertex)
                        return
                list.append(vertex)

    def depth_first_search(self):
        visited = [False] * self.number_of_vertex
        print(self.dfs(10, 3, visited))
        print(self.dfs(10, 3, visited))

    def dfs(self, vertex, end, visited):
        print("{} ->".format(vertex), end="")
        if vertex == end:
            return True
        visited[vertex] = True
        for i in self.adjacency_list[vertex]:
            if not visited[i]:
                return self.dfs(i, end, visited)


graph_instance = graph(100)
graph_instance.generate_edges()
for i in graph_instance.adjacency_list:
    print("{}: {}".format(i, graph_instance.adjacency_list[i]))
graph_instance.depth_first_search()
