import pandas as pd
import matplotlib.pyplot as plt
from Func_CW.adjacency_list_graph import AdjacencyListGraph
from task1a import find_shortest_path, stations_to_path

class LondonUndergroundStopsHistogram:
    """
    Class to analyze London Underground journeys in terms of stops. Loads data from
    an Excel file, builds an adjacency graph, calculates journey distances by stop count,
    finds the longest journey, and plots a histogram of journey lengths in stops.
    """

    def __init__(self, file_path):
        """
        Initializes placeholders for stations, journeys, graph, stops, and the longest journey.
        """
        self.file_path = file_path
        self.stations = []
        self.journeys = pd.DataFrame()
        self.adjGraph = None
        self.stop_counts = []
        self.longest_journey = {"start": "", "end": "", "path": "", "stops": 0}

    def load_data(self):
        """
        Loads data from the Excel file and separates unique stations and journeys.
        """
        df = pd.read_excel(self.file_path, header=None, names=["Line", "Station 1", "Station 2", "Time"])
        self.stations = list(df[df["Station 2"].isnull()]["Station 1"].unique())
        self.journeys = df[df["Station 2"].notnull()][["Station 1", "Station 2"]]


    def create_graph(self):
        """
        Creates an adjacency graph with edge weights of 1 to represent a single stop between stations.
        """
        self.adjGraph = AdjacencyListGraph(len(self.stations), directed=False, weighted=True)

        for index, row in self.journeys.iterrows():
            station_1 = self.stations.index(row["Station 1"])
            station_2 = self.stations.index(row["Station 2"])

            # Set edge weight to 1 to count each connection as one stop
            if not self.adjGraph.has_edge(station_1, station_2):
                self.adjGraph.insert_edge(station_1, station_2, 1)
            else:
                # Ensure weight remains 1 for stop-counting consistency
                old_edge = self.adjGraph.find_edge(station_1, station_2)
                old_edge.set_weight(1)

    def calculate_stop_counts(self):
        """
        Calculates the shortest path by stop count between all unique station pairs.
        Updates the longest journey if a journey exceeds the current longest stop count.
        """
        for x in range(len(self.stations)):
            for y in range(x + 1, len(self.stations)):
                stops, path = find_shortest_path(self.adjGraph, x, y)
                self.stop_counts.append(stops)

                # Update longest journey if the current stop count is greater
                if stops > self.longest_journey["stops"]:
                    self.longest_journey = {"start": x, "end": y, "path": path, "stops": stops}

    def display_longest_journey(self):
        """
        Displays details of the longest journey found, including start, end, and stop count.
        """
        start = self.stations[self.longest_journey["start"]]
        end = self.stations[self.longest_journey["end"]]
        path = self.longest_journey["path"]
        stops = self.longest_journey["stops"]

        print("Total journeys calculated:", len(self.stop_counts))
        print(f"The longest journey is from {start} to {end} with {stops} stops.")
        print("Path:", stations_to_path(path, self.stations))

    def plot_histogram(self):
        """
        Plots a histogram of journey lengths by the number of stops.
        """
        plt.hist(self.stop_counts, bins=range(1, max(self.stop_counts) + 1), edgecolor="black")
        plt.title("Histogram of journeys based on number of stops")
        plt.xlabel("Number of stops")
        plt.ylabel("Number of journeys")
        plt.show()

    def create_histogram(self):
        """
        Executes all methods: loads data, creates the graph, calculates stop counts,
        displays the longest journey, and plots the histogram.
        """
        self.load_data()
        self.create_graph()
        self.calculate_stop_counts()
        self.display_longest_journey()
        self.plot_histogram()


if __name__ == "__main__":
    graph = LondonUndergroundStopsHistogram("London Underground data(2).xlsx")
    graph.create_histogram()


