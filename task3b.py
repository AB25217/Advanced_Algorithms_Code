import pandas as pd 
from Func_CW.adjacency_list_graph import AdjacencyListGraph
from task1a import find_shortest_path, stations_to_path
import matplotlib.pyplot as plt
  
df = pd.read_excel("London_Underground_data.xlsx",
                   header=None, 
                   names=["Line", "Station 1", "Station 2", "Time"]) 

stations = df[df["Station 2"].isnull()] # Gets cells where third column is null
stations = list(stations["Station 1"].unique()) # Creates list of unique stations

journeys = df[df["Station 2"].notnull()] # Gets cells where third column is not null
journeys = journeys[["Station 1", "Station 2", "Time"]] # Panda datagram with three columns

adjGraph = AdjacencyListGraph(len(journeys.index), directed=False, weighted=True)

for index, row in journeys.iterrows(): # Iterates over panda datagram
    
    station_1 = stations.index(row["Station 1"])
    station_2 = stations.index(row["Station 2"])
    time = row["Time"]

    # Since some journeys exists on multiple line we check for existing edge before adding 
    if not adjGraph.has_edge(station_1, station_2): 
        adjGraph.insert_edge(station_1, station_2, 1) # change time to 1 to signify 1 stop
    else:
        old_edge = adjGraph.find_edge(station_1, station_2)
        old_edge.set_weight(1)

stop_count = []
longest_journey = {"start": "", "end": "", "path": "", "stops": 0}

'''
Loop runs over every element in the stations list creating unique journey pairs.
Starting with x + 1 in the inner loop ensure we don't have repeated or reversed pairs
so journeys are unqiue
'''

for x in range(len(stations)):
    for y in range(x + 1, len(stations)):
        stops, path = find_shortest_path(adjGraph, x, y)
        stop_count.append(stops)
        if stops > longest_journey["stops"]:
            longest_journey = {"start": x, "end": y, "path": path, "stops": stops}

print(stations_to_path(longest_journey["path"], stations))

plt.hist(stop_count, bins=range(1, max(stop_count) + 1))
plt.title("Histogram of journeys")
plt.xlabel("Number of stops")
plt.ylabel("Number of journeys")
plt.show() 

