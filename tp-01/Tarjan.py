import random
from timeit import Timer

class Digraph:
    
    vertex_list:list[list]

    def __init__(self, number_vertex) -> None:
        self.vertex_list = []
        self._create_digraph(number_vertex)
        
    def _create_digraph(self, number_vertex):
        self.number_vertex = number_vertex
        number_edge = number_vertex * random.randint(5, 10)
        
        if number_edge > number_vertex * (number_vertex - 1):
            print("ERROR2")

        self.vertex_list = [[] for _ in range(number_vertex)]

        vertex_counter = 0

        while vertex_counter < number_vertex:
            origin = random.randint(0, number_vertex - 1)
            destination = random.randint(0, number_vertex - 1)
            
            if destination not in self.vertex_list[origin] and destination != origin:
                self._add_edge(origin, destination)
                vertex_counter += 1

    def _add_vertex(self, vertex):
        if vertex not in self.vertex_list:
            self.vertex_list[vertex] = []

    def _add_edge(self, origin, destination):
        if origin in range(self.number_vertex) and destination in range(self.number_vertex):
            self.vertex_list[origin].append(destination)

        else:
            print("ERRO1!")

    def tarjan(self):
        self.ids = [-1 for _ in range(self.number_vertex)]
        self.low = [-1 for _ in range(self.number_vertex)]
        self.stack = []
        self.is_on_stack = set()
        self.components = []
        self.index = 0
        
        for v in range(self.number_vertex):
            if self.ids[v] == -1:
                self._tarjan(v)

        return self.components

    def _tarjan(self, vertex):
        self.ids[vertex] = self.index
        self.low[vertex] = self.index
        self.index += 1
        self.stack.append(vertex)
        self.is_on_stack.add(vertex)

        for neighbour in self.vertex_list[vertex]:
            if self.ids[neighbour] == -1:
                self._tarjan(neighbour)
                self.low[vertex] = min(self.low[vertex], self.low[neighbour])
            elif neighbour in self.is_on_stack:
                self.low[vertex] = min(self.low[vertex], self.ids[neighbour])

        if self.low[vertex] == self.ids[vertex]:
            component = []
            while True:
                node = self.stack.pop()
                self.is_on_stack.remove(node)
                component.append(node)
                if node == vertex:
                    break

            self.components.append(component)
            
    
    def print_graph(self):
        for vertex in self.vertex_list:
            print(vertex)
            
def get_time():
    graph = Digraph(1000)
    
t = Timer("get_time()", globals=globals())
num_tests = 1000
total_time = t.timeit(number=num_tests)
average_time = total_time / num_tests

print("Total_time:", total_time)
print("Average_time:", average_time)
            

#graph.print_graph()