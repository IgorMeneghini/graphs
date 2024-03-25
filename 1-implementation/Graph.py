class graph:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self._read_file()

    def _start_matrix(self, size):
        self.adjacency_matrix = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(0)
            self.adjacency_matrix.append(row)

    def _read_file(self):
        try:
            with open(self.file_path, "r") as file:
                first_line = file.readline().strip()
                number_of_vertex, number_of_edges = map(int, first_line.split())
                self._start_matrix(number_of_vertex)
                for line_number, line in enumerate(file):
                    origin, destination = map(int, line.strip().split())
                    self.adjacency_matrix[origin - 1][destination - 1] = 1
        except Exception as e:
            print(e)

    def _calculate_exit_grade(self):
        print("(i)Exit Grade:")
        for i, row in enumerate(self.adjacency_matrix):
            exit_grade = sum(1 for edge in row if edge != 0)
            print(f"{i+1}: {exit_grade}")

    def _calculate_entry_grade(self):
        print("(ii)Entry Grade")
        for i in range(len(self.adjacency_matrix[0])):
            entry_grade = 0
            for j in range(len(self.adjacency_matrix)):
                if self.adjacency_matrix[j][i] != 0:
                    entry_grade += 1
            print(f"{i+1}: {entry_grade}")

    def set_of_successors(self):
        print("(iii) Set of Successors:")
        for i in range(len(self.adjacency_matrix)):
            successors = []
            for j in range(len(self.adjacency_matrix[0])):
                if self.adjacency_matrix[i][j] != 0:
                    successors.append(j + 1)
            print(f"{i+1}: {successors}")

    def set_of_predecessors(self):
        print("(iiii) Set of Predecessors:")
        for i in range(len(self.adjacency_matrix[0])):
            predecessors = []
            for j in range(len(self.adjacency_matrix)):
                if self.adjacency_matrix[j][i] != 0:
                    predecessors.append(j + 1)
            print(f"{i+1}: {predecessors}")


graph_instance = graph("graph-test-100-1.txt")
# print(graph_instance.adjacency_matrix)
# graph_instance._calculate_exit_grade()
# graph_instance._calculate_entry_grade()
graph_instance.set_of_successors()
# graph_instance.set_of_predecessors()
