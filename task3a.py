'''
Histogram for London Underground journeys 
* Import data from excel file
* Create adjacency graph for unqiue journeys
* Calculate distances from every station to another
* Create histogram from distances
* Find the longest journey path and time
'''

import pandas as pd
import matplotlib.pyplot as plt
from Func_CW.adjacency_list_graph import AdjacencyListGraph
from task1a import find_shortest_path_task1, stations_to_path

class London_Underground_Histogram:
    """
    Class to extract London Underground journeys. Loads data from excel file, builds an 
    adjacency graph, calculates journey distances, finds the longest journey, and plots a 
    histogram of journey times.
    """
    
    def __init__(self, file_path):
        """
        Sets up placeholders for stations, journeys, graph, distances, and the longest journey
        """
        self.file_path = file_path
        self.stations = []
        self.journeys = pd.DataFrame()
        self.adjGraph = None
        self.distances = []
        self.longest_journey = {"start": "", "end": "", "path": "", "distance": 0}
    
    def load_data(self):
        """
        Extracts data from the excel file provided
        Separates the list of unique stations and journeys with times
        """
        df = pd.read_excel(self.file_path, header=None, names=["Line", "Station 1", "Station 2", "Time"])
        self.stations = list(df[df["Station 2"].isnull()]["Station 1"].unique())
        self.journeys = df[df["Station 2"].notnull()][["Station 1", "Station 2", "Time"]]
    
    def create_graph(self):
        """
        Creates an adjacency graph of the journeys
        """
        self.adjGraph = AdjacencyListGraph(len(self.journeys.index), directed=False, weighted=True)
        
        for index, row in self.journeys.iterrows():
            station_1 = self.stations.index(row["Station 1"])
            station_2 = self.stations.index(row["Station 2"])
            time = row["Time"]
            
            # Add edge only if it does not already exist or has a longer time than the new time
            if not self.adjGraph.has_edge(station_1, station_2):
                self.adjGraph.insert_edge(station_1, station_2, time)
            else:
                old_edge = self.adjGraph.find_edge(station_1, station_2)
                if old_edge.get_weight() > time:
                    old_edge.set_weight(time)
    
    def calculate_distances(self):
        """
        Calculates the shortest distance between all unique station pairs
        Updates the longest journey if a journey exceeds the current longest distance
        """
        for x in range(len(self.stations)):
            for y in range(x + 1, len(self.stations)):
                path, d = find_shortest_path_task1(self.adjGraph, x, y)
                self.distances.append(d)
                
                # Update longest journey if the current distance is greater
                if d > self.longest_journey["distance"]:
                    start = self.stations[x]
                    end = self.stations[y]
                    self.longest_journey = {"start": start, "end": end, "path": path, "distance": d}
    
    def display_longest_journey(self):
        """
        Displays the details of the longest journey found, including start, end, and distance
        """
        start = self.longest_journey["start"]
        end = self.longest_journey["end"]
        path = self.longest_journey["path"]
        distance = self.longest_journey["distance"]
        
        print("Total journeys calculated:", len(self.distances))
        print("The longest journey is from", start, "to", end, "lasting", distance, "minutes")
        print(stations_to_path(path, self.stations))
    
    def plot_histogram(self):
        """
        Plots a histogram of the journey distances
        """
        plt.hist(self.distances)
        plt.title("Histogram of journeys")
        plt.xlabel("Distance (in minutes)")
        plt.ylabel("Number of journeys")
        plt.show()
    
    def create_histogram(self):
        """
        Executes all other functions: loads data, creates the graph,
        calculates distances, displays the longest journey, and plots the histogram
        """
        self.load_data()
        self.create_graph()
        self.calculate_distances()
        self.display_longest_journey()
        self.plot_histogram()


if __name__ == "__main__":
    graph = London_Underground_Histogram("London Underground data OG.xlsx")
    graph.create_histogram()
