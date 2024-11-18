from task1b_measurements import measure_algorithm_time  # measurement algorithm from task1b measurements
import matplotlib.pyplot as graph  # using to plot the results onto a graph

# code execution below
if __name__ == '__main__':
    measurements = measure_algorithm_time(100, 1000, 100)  # collect the measurements
    x_labels = []  # x values will contain the sizes n and the number of edges in string format
    y_values = []  # y values contain the average execution time of the measurement

    for i in measurements:  # for each measurement
        x_labels.append(f"{i[0]} nodes, {i[1]} edges")  # append the graph size and edge number of the measurement into the x values list
        temp = i[2:]  # temporary list which slices the graph size and edge number from the actual execution time measurements
        avg_time = sum(temp) / len(temp)  # calculate the average execution time
        y_values.append(avg_time)  # add the average execution time to the y_values

    x_indices = range(len(x_labels))  # create an index array for the x-axis

    graph.figure(figsize=(10, 5))  # figure size for the graph screen 
    graph.plot(x_indices, y_values, marker='o')  # plotting the indices and y values
    graph.xticks(x_indices, x_labels, rotation=45)  # set x-axis labels to the formatted strings
    graph.title("Average Execution Time vs Graph Size and Edge Count")  # title of screen 
    graph.xlabel("Graph Size (nodes and edges)")  # x label
    graph.ylabel("Average Execution Time (seconds)")  # y label
    graph.grid(True)
    graph.tight_layout()  # optional: adjust layout to prevent label overlap
    graph.show()

