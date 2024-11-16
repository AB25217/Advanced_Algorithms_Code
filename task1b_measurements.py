from task1a import find_shortest_path
from task1b_graphgenerator import GenerateGraph
import time
import random

if __name__ == '__main__':
    graph_generator = GenerateGraph()
    n = 100  # initial number of vertices

    while n <= 1000:
        generated_graph = graph_generator.graph_generator(n, 0.15, True, False, True, 2, 15)
        results = [n]  # index 0 represents the vertices n for the graph; rest represent the result
        execution_times = [n]  # index 0 represents the vertices n for the graph; rest represent the execution times

        for _ in range(10):  # run 10 times
            start_time = time.time()
            results.append(find_shortest_path(generated_graph, random.randint(0, n), random.randint(0, n)))
            execution_times.append(time.time() - start_time)

        print(results)
        print(execution_times)
        n += 100
