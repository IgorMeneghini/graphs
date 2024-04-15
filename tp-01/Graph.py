import random
from timeit import Timer


class graph:
    def __init__(self, number_of_vertices) -> None:
        # Initialize the graph with a given number of vertices
        self.number_of_vertices = number_of_vertices
        # Create an empty adjacency list to store the graph's edges
        self.adjacency_list = self._start_list()
        # Generate random edges for the graph
        self.generate_edges()

    def _start_list(self):
        # Create an empty adjacency list with vertices numbered from 0 to (number_of_vertices - 1)
        adjacency_list = {}
        for i in range(self.number_of_vertices):
            adjacency_list[i] = []
        return adjacency_list

    def generate_edges(self):
        # Generate random edges for each vertex in the graph
        for i in range(self.number_of_vertices):
            # Generate a random number to represent the degree of the vertex
            random_vertex_degree = random.randrange(0, self.number_of_vertices - 1)
            # Add edges to the current vertex until its degree is reached
            while len(self.adjacency_list[i]) < random_vertex_degree:
                # Generate a random vertex to connect to
                random_vertex = random.randrange(0, self.number_of_vertices)
                # Check if the randomly chosen vertex is not already adjacent to the current vertex
                if random_vertex not in self.adjacency_list[i]:
                    # Add the edge between the current vertex and the random vertex
                    self.adjacency_list[i].append(random_vertex)
                    self.adjacency_list[random_vertex].append(i)
            print(i)

    # Depth First Search (DFS) method
    def depth_first_search(self):
        # Initialize a list to keep track of visited vertices
        visited = [False] * self.number_of_vertices
        # Perform DFS from two random starting vertices and print the path
        print(
            self.dfs(
                random.randrange(0, self.number_of_vertices - 1),
                random.randrange(0, self.number_of_vertices - 1),
                visited,
            )
        )
        print(
            self.dfs(
                random.randrange(0, self.number_of_vertices - 1),
                random.randrange(0, self.number_of_vertices - 1),
                visited,
            )
        )

    # Recursive function for DFS
    def dfs(self, vertex, end, visited):
        # Print the current vertex and mark it as visited
        print("{} ->".format(vertex), end="")
        # If the end vertex is reached, return True
        if vertex == end:
            return True
        visited[vertex] = True
        # Recursively visit adjacent vertices
        for neighbor in self.adjacency_list[vertex]:
            if not visited[neighbor]:
                if self.dfs(neighbor, end, visited):
                    return True
        return False

    # Find articulation points method
    def find_articulations(self):
        # Initialize a list to store articulation points
        articulations = []
        # Iterate through each vertex in the graph
        for i in range(len(self.adjacency_list)):
            # Initialize a list to track visited vertices
            visited = [False] * (self.number_of_vertices)
            # Perform DFS from the current vertex excluding it, to find articulation points
            self.dfs_articulations(visited, i, 0)
            # Check if all vertices are visited after excluding the current vertex
            for j in range(len(self.adjacency_list)):
                if j != i:
                    if not visited[j]:
                        # If not all vertices are visited, add the current vertex to the list of articulation points
                        articulations.append(i)
                        break
        return articulations

    # Recursive function to find articulation points
    def dfs_articulations(self, visited, removed_vertex, vertex=0):
        # Mark the current vertex as visited
        visited[vertex] = True
        # Visit all adjacent vertices except the one that has been removed
        for i in self.adjacency_list[vertex]:
            if not visited[i] and i != removed_vertex:
                self.dfs_articulations(visited, removed_vertex, i)


graph_instance = graph(100000)


# Test function for DFS


def test_art():
    # graph_instance.depth_first_search()
    articulations = graph_instance.find_articulations()
    print(articulations)


t = Timer("test_art()", globals=globals())
num_tests = 100
total_time = t.timeit(number=num_tests)
average_time = total_time / num_tests

print(
    f"Metodo2: Average execution time over {num_tests} tests: {average_time:.6f} seconds"
)


def test_dfs():
    graph_instance.depth_first_search()


j = Timer("test_dfs()", globals=globals())
num_tests = 100
total_time = j.timeit(number=num_tests)
average_time = total_time / num_tests

print(
    f"Metodo 1: Average execution time over {num_tests} tests: {average_time:.6f} seconds"
)


# Uncomment the following lines to find articulation points
