import pandas as pd
import matplotlib.pyplot as plt
from Func_CW.adjacency_list_graph import AdjacencyListGraph
from task1a import find_shortest_path, _stations_to_path  # Using functions from Task 1a
from task4a import Graph_From_CSV, ClosedRoutes  # Using classes from Task 4a


def create_histogram_and_longest_path(graph, stations):
    """
    Creates a histogram of journey durations and identifies the longest path.
    The graph represents the reduced London Underground network, calculates the shortest path in minutes using
    dijkstra on the already reduced network, stores these journeys in a list and creates a histogram.
    The function finds the longest path by updating everytime a longer journey is found and displays the start
    station, end station, the whole path and the duration in minutes.
    """
    distances = []
    longest_journey = {"start": "", "end": "", "path": "", "distance": 0}

    # Compute the shortest paths between all pairs of stations
    for x in range(len(stations)):
        for y in range(x + 1, len(stations)):
            d, path = find_shortest_path(graph, x, y)
            distances.append(d)
            # Update longest journey if this path is longer
            if d > longest_journey["distance"]:
                longest_journey = {"start": x, "end": y, "path": path, "distance": d}

    # Display the longest path in the reduced network
    print("Longest journey in reduced network:")
    print(_stations_to_path(longest_journey["path"], stations))
    print("Duration:", longest_journey["distance"], "minutes")

    # Plot the histogram of journey durations
    plt.hist(distances, bins=20, edgecolor='black')
    plt.title("Reduced Network Journey Duration Histogram")
    plt.xlabel("Journey Duration (minutes)")
    plt.ylabel("Frequency")
    plt.show()


if __name__ == "__main__":
    # Creating the initial graph from the provided Excel file
    graph_data = Graph_From_CSV('London Underground data.xlsx')
    graph_data.create_graph()

    # Identifying routes to close using Task 4a's method
    closed_routes = ClosedRoutes(graph_data.graph, graph_data.station_list)
    closed_routes_set, _ = closed_routes.find_what_routes_to_close(named_list=True)

    # Removing the identified closed routes from the graph
    for edge in closed_routes_set:
        graph_data.graph.delete_edge(edge[0], edge[1])

    # Plots the histogram and identifies the longest path
    create_histogram_and_longest_path(graph_data.graph, graph_data.station_list)
