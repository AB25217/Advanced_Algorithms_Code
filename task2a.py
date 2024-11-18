from Func_CW.adjacency_list_graph import AdjacencyListGraph
from Func_CW.dijkstra import dijkstra

#0 = Victoria
#1 = Green Park
#2 = St James Park
#3 = Westminster
#4 = Waterloo
#5 = Enbarkment
#6 = Charing Cross
#7 = Picadilly Circus
#8 = Oxford Circus
#9 = Bond Street

#list of stations
stations = ["Victoria", "Green Park", "St James Park", "Westminster", "Waterloo", "Enbarkment", "Charing Cross", "Picadilly Circus", "Oxford Circus", "Bond Street"]

# calling adjGraph
adjGraph = AdjacencyListGraph(10, directed=False, weighted=True)


# inserting all edges between train stations, with repsective weights
adjGraph.insert_edge(0, 1, weight=2)
adjGraph.insert_edge(0, 2, weight=2)
adjGraph.insert_edge(2, 3, weight=2)
adjGraph.insert_edge(3, 1, weight=2)

adjGraph.insert_edge(3, 4, weight=2)
adjGraph.insert_edge(3, 5, weight=1)
adjGraph.insert_edge(4, 5, weight=2)
adjGraph.insert_edge(5, 6, weight=1)
adjGraph.insert_edge(6, 7, weight=2)
adjGraph.insert_edge(7, 1, weight=2)

adjGraph.insert_edge(7, 8, weight=2)
adjGraph.insert_edge(8, 1, weight=2)
adjGraph.insert_edge(8, 9, weight=2)
adjGraph.insert_edge(9, 1, weight=2)

# list of all edges between stations
print(adjGraph.get_edge_list())

def find_shortest_path(graph, start, end):
  """
  Function to find shortest path between two stations in a graph based on their edges weights

  Attributes:
  graph: Adjacency_list graph
  start: int starting station
  end: int ending station


  return:
    distance = int distance between stations

    path = list all previous stations, if any
  """

  d, pi = dijkstra(graph, start)

  distance = d[end] # distance between start and end stations

  current = end # the preedeccessor of end station

  path = []  # the path between start and end
  

  while current != None:
    path.append(current)
    current = pi[current]

  path.reverse()
  stops  = len(path) - 1 # calculate the number of stops as the length of the path minus one
  return stops, path

  

def stations_to_path(path, stations):
    """
    Function for converting a list of station indices (path) to their respective station names, returning a string with arrows.

    Parameters:
        path (list): List of station indices in the path, from find_shortest_path
        stations (list): List of station names corresponding to indices

    Returns:
        path_str (str): String representation of the path with station names separated by arrows
    """
    #path_str list where station names are mapped with predecessor indices
    path_str = [stations[i] for i in path]

    # Join station names with arrows
    return " -> ".join(path_str)




if __name__ == "__main__":
    # display index of stations from 0 - 9
    print("Available stations:")
    for i, station in enumerate(stations):
        print(f"{i}: {station}")

    # loop for user input
    while True:
        start = int(input("Enter the starting station number: "))
        end = int(input("Enter the destination station number: "))

        # check input
        if 0 <= start < len(stations) and 0 <= end < len(stations):
                break
        else:
                print("Station number out of range. Please try again.")
    else:
          print("Invalid input. Please enter valid numbers.")


   # display results
    stops, path = find_shortest_path(adjGraph, start, end)
    print(f"Number of stops from {stations[start]} to {stations[end]}: {stops}")
    print("Path:", stations_to_path(path, stations))
