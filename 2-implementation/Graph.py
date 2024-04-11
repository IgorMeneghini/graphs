class graph:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self._read_file()
        self.discovery_time = [0] * (len(self.adjacency_list) + 1)
        self.end_time = [0] * (len(self.adjacency_list) + 1)
        self.father = [None] * (len(self.adjacency_list) + 1)
        self.global_time = 0
        self.tree_edges = []
        self.return_edges = []
        self.crossing_edges = []
        self.leading_edges = []

    def _start_list(self, size):
        self.adjacency_list = {}
        for i in range(size + 1):
            self.adjacency_list[i] = []

    def _read_file(self):
        try:
            with open(self.file_path, "r") as file:
                first_line = file.readline().strip()
                number_of_vertices, _ = map(int, first_line.split())
                self._start_list(number_of_vertices)
                for line in file:
                    origin, destination = map(int, line.strip().split())
                    self._insertion_sort(self.adjacency_list[origin], destination)
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except ValueError:
            print("Invalid data format in the file.")

    def _insertion_sort(self, list, destination):
        if destination not in list:
            if not list:
                list.append(destination)
            else:
                for i in range(len(list)):
                    if list[i] > destination:
                        list.insert(i, destination)
                        return
                list.append(destination)

    def _depth_first_search(self, vertex=0):
        for i in range(len(self.adjacency_list)):
            if self.discovery_time[i] == 0:
                self._dfs_visit(i)

    def _dfs_visit(self, vertex):
        self.global_time += 1
        self.discovery_time[vertex] = self.global_time
        for i in self.adjacency_list[vertex]:
            if self.discovery_time[i] == 0:
                self.tree_edges.append((vertex, i))
                self.father[i] = vertex + 1
                self._dfs_visit(i)
            else:
                if self.end_time[i] == 0:
                    self.return_edges.append((vertex, i))
                elif self.discovery_time[vertex] < self.discovery_time[i]:
                    self.leading_edges.append((vertex, i))
                else:
                    self.crossing_edges.append((vertex, i))
        self.global_time += 1
        self.end_time[vertex] = self.global_time

    def _get_edge_classification(self, vertex):
        print(f"Vertex {vertex}: {self.adjacency_list[vertex]}")
        for i in self.adjacency_list[vertex]:
            if (vertex, i) in self.tree_edges:
                print(f"{(vertex, i )} is a Tree edge")
            elif (vertex, i) in self.return_edges:
                print(f"{(vertex, i )} is a Return edge")
            elif (vertex, i) in self.leading_edges:
                print(f"{(vertex, i )} is a leading edge")
            else:
                print(f"{(vertex, i )} is a crossing edge")


graph_instance = graph("graph-test-100-1.txt")
for vertex in range(1, len(graph_instance.adjacency_list)):
    print(f"Vertex {vertex}: {graph_instance.adjacency_list[vertex]}")

graph_instance._depth_first_search()
# print("Discovery_time:", graph_instance.discovery_time, "\n")
# print("end_time:", graph_instance.end_time, "\n")
# print("father:", graph_instance.father, "\n")
graph_instance._get_edge_classification()
print(f"Tree Edges: {graph_instance.tree_edges}")
