import random

class graph:
    def __init__(self) -> None:
        self.number_of_vertex = 100

    def _start_list(self):
        self.adjacency_list = {}
        for i in range(self.number_of_vertex):
            self.adjacency_list[i] = []

        for i in range(self.number_of_vertex):
            random_vertex_degree = random.randrange(0,self.number_of_vertex - 2)
            
            for j in range(random_vertex_degree):

                random_vertex = random.randrange(0,self.number_of_vertex - 1)
                if random_vertex not in self.adjacency_list[i]:
                    self.adjacency_list[i].append(random_vertex)
                    self.adjacency_list[random_vertex].append(i)
            #print(random_vertex)


graph_instance = graph()
graph_instance._start_list()
