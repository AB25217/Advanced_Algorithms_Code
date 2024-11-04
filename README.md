from Func_CW.generate_random_graph import generate_random_graph # FROM THE COURSEWORK GIVEN LIBRARY
import random
import time  # Importing the time module to measure execution time

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

        # Parameters validation check
        if (weighted == True) and (min_weight > max_weight):
            raise ValueError("min_weight cannot be larger than max_weight")  # Check if min_weight is less than max_weight

        if type(v) != int:
            raise ValueError("V needs to be an integer")  # Ensure v is an integer
        if type(edge_prob) != float and type(edge_prob) != int:
            raise ValueError("edge_prob needs to be either int or float")  # Ensure edge_prob is a number

        if type(weighted) != bool or type(directed) != bool:
            raise ValueError("weighted and directed need to be bool values")  # Ensure weighted and directed are booleans

        # If validations pass
        else: 
            self.graph = generate_random_graph(v, edge_prob, by_list, directed, weighted, min_weight, max_weight) # Create the graph with the generate random graph algorithm
            return self.graph  # Return the generated graph

    def measure_execution_time(self, n, edge_prob, by_list, directed, weighted, min_weight, max_weight):  # Measure execution time
        start_time = time.time()  # Start timing
        self.graph = self.graph_generator(n, edge_prob, by_list, directed, weighted, min_weight, max_weight)  # Generate the graph
        execution_time = time.time() - start_time  # Calculate execution time
        return execution_time  # Return the execution time

# Testing 
if __name__ == '__main__': 
    generate_graph = GenerateGraph()  # Create an instance of GenerateGraph
    for n in range(1100, 2100, 100):  # Loop through the specified range
        execution_time = generate_graph.measure_execution_time(n, 0.15, True, False, True, 2, 15)  # Measure execution time for each n
        print(f"Number of stops: {n}, Execution time: {execution_time:.4f} seconds")  # Print the execution time

