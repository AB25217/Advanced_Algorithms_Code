from task1b_measurements import measure_algorithm_time # measurement algorithm from task1b measuremnets
import matplotlib.pyplot as graph  # using to plot the results onto a graph

# code execution below
if __name__ == '__main__':
    measurements = measure_algorithm_time(100,1000,100) # collect the measurements
    x_values = [] # x values will contain the sizes n and the number of edges in string format
    y_values = [] # y values contain the average execution time of the measurement
    for i in measurements: # for each measurement
        x_values.append(f"{i[0]} nodes, {i[1]} edges") # append the graph size and edge number of the measurement into the x values list
        temp = i[2:] # temporary list which slices the graph size and edge number form the actual execution time measurements
        y_values.append(str(sum(temp) / len(temp))) # add the average of the execution times to the y_values

    graph.plot(x_values, y_values, marker='o')
    graph.title('Execution Time Measurements for Djikstra Algorithm')
    graph.xlabel('Graph Size & Number of Edges')
    graph.ylabel('Measurement Average')
    graph.show()
