import pandas as pd 
from Func_CW.adjacency_list_graph import AdjacencyListGraph
from Task_1a import find_shortest_path, stations_to_path
import matplotlib.pyplot as plt
  
df = pd.read_excel("london_underground_data.xlsx", 
                   header=None, 
                   names=["Line", "Station 1", "Station 2", "Time"]) 

stations = df[df["Station 2"].isnull()]
stations = list(stations["Station 1"].unique())

journeys = df[df["Station 2"].notnull()]
journeys = journeys[["Station 1", "Station 2", "Time"]]

adjGraph = AdjacencyListGraph(len(journeys.index), directed=False, weighted=True)

for index, row in journeys.iterrows():
    
    station_1 = stations.index(row["Station 1"])
    station_2 = stations.index(row["Station 2"])
    time = row["Time"]

    try: 
        adjGraph.insert_edge(station_1, station_2, time)
    except:
        print("Duplicate:", row["Station 1"], row["Station 2"], time)

completed_pairs = []
distances = []
longest_journey = {"start": "", "end": "", "path": "", "distance": 0}

for x in range(len(stations)):
    for y in range(len(stations)):
        if not x == y and [x, y] not in completed_pairs and [y, x] not in completed_pairs:
            d, path = find_shortest_path(adjGraph, x, y)
            completed_pairs.append([x, y])
            distances.append(d)
            if d > longest_journey["distance"]:
                longest_journey = {"start": x, "end": y, "path": path, "distance": d}

print(stations_to_path(longest_journey["path"], stations))
plt.hist(distances)
plt.show() 
