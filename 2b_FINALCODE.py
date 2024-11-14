from Func_CW.generate_random_graph import generate_random_graph # FROM THE COURSEWORK GIVEN LIBRARY
import random
import time  # Importing the time module to measure execution time
import matplotlib.pyplot as plt  # Importing matplotlib for visualization
from Func_CW.dijkstra import dijkstra

class GenerateGraph:
    def __init__(self):  # Constructor to initialize the graph
        self.graph = None  # Represents the graph

    def graph_generator(self, v, edge_prob, by_list, directed, weighted, min_weight, max_weight):
        """
        Creates a random graph based on the parameters specified.
        Arguments: 
        v(int): the number of vertices in the graph
        edge_prob(num): the probability of one vertex to have an edge with another vertex
        by_list(bool): True if graph to be in adjacency list, false if for matrix form
        directed(bool): True for graph to be directed, false otherwise
        weighted(bool): True for the graph to be weighted, false otherwise
        min_weight(int): What is the minimum weight of the graph, if any
        max_weight(int): What is the maximum weight for an edge, if any
        """

        "Parameters validation check"
        if weighted and (min_weight > max_weight):
            raise ValueError("min_weight cannot be larger than max_weight")  # Check if min_weight is less than max_weight

        if not isinstance(v, int) or v <= 0:
            raise ValueError("V needs to be a positive integer")  # Ensure v is a positive integer
        if not isinstance(edge_prob, (float, int)) or not (0 <= edge_prob <= 1):
            raise ValueError("edge_prob needs to be a float between 0 and 1 or an integer")  # Ensure edge_prob is a valid probability

        if not isinstance(weighted, bool) or not isinstance(directed, bool):
            raise ValueError("weighted and directed need to be bool values")  # Ensure weighted and directed are booleans

        "If validations pass"
        self.graph = generate_random_graph(v, edge_prob, by_list, directed, weighted, min_weight, max_weight) # Create the graph with the generate random graph algorithm
        return self.graph  # Return the generated graph

    def measure_execution_time(self, n, edge_prob, by_list, directed, weighted, min_weight, max_weight, num_trials=10):
        """
        Measures the average execution time of running Dijkstra's algorithm on randomly selected pairs of vertices.
        Arguments:
        n(int): the number of vertices in the graph
        edge_prob(num): the probability of one vertex to have an edge with another vertex
        by_list(bool): True if graph to be in adjacency list, false if for matrix form
        directed(bool): True for graph to be directed, false otherwise
        weighted(bool): True for the graph to be weighted, false otherwise
        min_weight(int): What is the minimum weight of the graph, if any
        max_weight(int): What is the maximum weight for an edge, if any
        num_trials(int): The number of trials to randomly select pairs and measure execution time
        Returns:
        float: The average execution time of running Dijkstra's algorithm
        """
        self.graph = self.graph_generator(n, edge_prob, by_list, directed, weighted, min_weight, max_weight)  # Generate the graph
        total_execution_time = 0

        for _ in range(num_trials):
            "Randomly select a pair of different vertices (source, destination)"
            source = random.randint(0, n - 1)
            destination = random.randint(0, n - 1)
            while destination == source:
                destination = random.randint(0, n - 1)

            "Measure execution time for Dijkstra's algorithm from source to destination"
            start_time = time.time()
            dijkstra(self.graph, source)  # Execute Dijkstra's algorithm starting from the source vertex
            execution_time = time.time() - start_time
            total_execution_time += execution_time

        average_execution_time = total_execution_time / num_trials  # Calculate average execution time
        return average_execution_time  # Return the average execution time

# Testing 
if __name__ == '__main__': 
    generate_graph = GenerateGraph()  # Create an instance of GenerateGraph
    num_vertices = list(range(1100, 2100, 100))  # List to hold the number of vertices
    execution_times = []  # List to hold the average execution times

    for n in num_vertices:  # Loop through the specified range
        print(f"Generating graph for n = {n}")  # Debugging output
        try:
            average_execution_time = generate_graph.measure_execution_time(n, 0.15, True, False, True, 2, 15, num_trials=10)  # Measure average execution time for each n
            execution_times.append(average_execution_time)  # Store the average execution time
            print(f"Number of vertices: {n}, Average Execution time: {average_execution_time:.4f} seconds")  # Print the average execution time
        except ValueError as e:
            print(f"Error occurred: {e}")  # Print the error if one occurs

    # Visualization of the execution times
    plt.figure(figsize=(10, 6))
    plt.plot(num_vertices, execution_times, marker='o', linestyle='-', color='b')
    plt.xlabel('Number of Vertices')
    plt.ylabel('Average Execution Time (seconds)')
    plt.title('Average Execution Time of Dijkstra Algorithm vs Number of Vertices')
    plt.grid(True)
    plt.show()
