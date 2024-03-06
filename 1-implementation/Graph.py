class graph:
    def __init__(self, size, file_path) -> None:
        self.file_path = file_path
        self._start_matrix(size)
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
                for line_number, line in enumerate(file):
                    if line_number == 0:
                        continue
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
                    entry_grade +=1
            print(f"{i+1}: {entry_grade}")

    



graph_instance = graph(100, "graph-test-100-1.txt")
print(graph_instance.adjacency_matrix)
graph_instance._calculate_exit_grade()
graph_instance._calculate_entry_grade()
