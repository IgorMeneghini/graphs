import random


class graph:
    def __init__(self, number_of_vertex) -> None:
        self.number_of_vertex = number_of_vertex

    def _start_list(self):
        self.adjacency_list = {}
        for i in range(self.number_of_vertex):
            self.adjacency_list[i] = []

        for i in range(self.number_of_vertex):
            random_vertex_degree = random.randrange(0, self.number_of_vertex - 2)

            for j in range(random_vertex_degree):

                random_vertex = random.randrange(0, self.number_of_vertex - 1)
                if random_vertex not in self.adjacency_list[i]:
                    self.adjacency_list[i].append(random_vertex)
                    self.adjacency_list[random_vertex].append(i)

    def depth_first_search(self):
        self.global_time = 0
        discovery_time = [0] * self.number_of_vertex
        end_time = [0] * self.number_of_vertex
        father = [None] * self.number_of_vertex
        for index, value in enumerate(discovery_time):
            if value == 0:
                self.dfs_visit(index, discovery_time, end_time, father)
        print(discovery_time)
        print(end_time)
        print(father)

    def dfs_visit(self, vertex, discovery_time, end_time, father):
        self.global_time += 1
        discovery_time[vertex] = self.global_time
        for i in self.adjacency_list[vertex]:
            if discovery_time[i] == 0:
                father[i] = vertex
                self.dfs_visit(i, discovery_time, end_time, father)
        self.global_time +=1
        end_time[vertex] = self.global_time



graph_instance = graph(100)
graph_instance._start_list()
graph_instance.depth_first_search()
