from task1a import find_shortest_path_task1
from task1b_graphgenerator import GenerateGraph
import time
import random

def measure_algorithm_time(start_vertices, end_vertices,increments,measurements_for_graph_size=10):
    """
    Desc: function measures an chosen graph algorithm based on starting vertice size, end vertice size, increments per each size 
    and ammount of measurements for each size n

    Parameters:
                start_vertices(int): the number of vertices to measure at the start
                end_vertices(int): the number of vertices to measure at the end 
                increments(int): how much to increment between start to end
                measurements_for_graph_size(int): How much to meausre per each graph size n. Default set at 10
                
    Returns:
            Execution_Time(list): 2D list containing measurements times for each graph size n,number of edges e at index 1, ] and its measurements, with all values being float
    """
    # Validation checking
    if type(start_vertices) != int or type(end_vertices) != int or type(measurements_for_graph_size) != int:
        raise ValueError("Please enter int values for start_vertices, end_vertices and measurements_for_graph_size")
    if  start_vertices > end_vertices:
        raise ValueError("end vertice parameter must be larger than start_vertice parameter")
    

    # start of code
    graph_generator = GenerateGraph() # generates a graph
    n = start_vertices # sets n as start_vertices for data manipulation
    execution_times = [] # stores all execution times for all graph sizes n
    while n <= end_vertices: # while the specified start(or n ) is not above the specified limitm
        generated_graph = graph_generator.graph_generator(n, 0.25, True, False, True, 2, 15)
        execution_time = [n, generated_graph.get_card_E()]  # index 0 represents the vertices n for the graph; 1 represents number of edges, rest represent the execution times

        for _ in range(measurements_for_graph_size):  # run 10 times
            start_time = time.time()
            find_shortest_path_task1(generated_graph, (random.randint(0, n) - 1), (random.randint(0, n) - 1)) # run the algorihtm with 2 random positions on the generated graph 
            execution_time.append(time.time() - start_time)
        execution_times.append(execution_time)
        n += increments
    return execution_times
    
if __name__ == '__main__':
    print(measure_algorithm_time(100, 1000, 100))