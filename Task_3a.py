import pandas as pd 
from Func_CW.adjacency_list_graph import AdjacencyListGraph
from Task_1a import find_shortest_path, stations_to_path
import matplotlib.pyplot as plt
  
df = pd.read_excel("london_underground_data.xlsx", 
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
        adjGraph.insert_edge(station_1, station_2, time)
    else:
        old_edge = adjGraph.find_edge(station_1, station_2)
        if old_edge.get_weight() > time: # If new time is lower then change weight
            old_edge.set_weight(time)

distances = []
longest_journey = {"start": "", "end": "", "path": "", "distance": 0}

'''
Loop runs over every element in the stations list creating unique journey pairs.
Starting with x + 1 in the inner loop ensure we don't have repeated or reversed pairs
so journeys are unqiue
'''

for x in range(len(stations)):
    for y in range(x + 1, len(stations)):
        d, path = find_shortest_path(adjGraph, x, y)
        distances.append(d)
        if d > longest_journey["distance"]:
            longest_journey = {"start": x, "end": y, "path": path, "distance": d}

print(stations_to_path(longest_journey["path"], stations))

plt.hist(distances)
plt.title("Histogram of journeys")
plt.xlabel("Distance (in minutes)")
plt.ylabel("Number of journeys")
plt.show() 

