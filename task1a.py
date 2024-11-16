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
stations_1 = ["Victoria", "Green Park", "St James Park", "Westminster", "Waterloo", "Enbarkment", "Charing Cross", "Picadilly Circus", "Oxford Circus", "Bond Street"]

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

    current = end # the predessecors of end station

    path = []  # the path between start and end

    while current != None: # while there are predecessors
      path.append(current) # append the current station to the path
      current = pi[current] # assign the current station to the current station of the path 

    path.reverse() # reverse the arr, as the structure is supposed to be from the start of the station to the end
    return path, distance 

def _stations_to_path(path, stations):
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
    start = 0  # Victoria station
    end = 6    # Charing Cross Station
    path, d = find_shortest_path(adjGraph, start, end)  # path and distance
    print(type(d))
    path_str = _stations_to_path(path, stations_1)  # get the formatted path as a string
    print(f"{stations_1[end]}: Distance = {d}, Path = {path_str}") # prints the distance and the path to the chosen stations 

    #testing from charing cross station to victoria station
    start = 6 
    end = 0
    path, d = find_shortest_path(adjGraph, start, end)
    path_str = _stations_to_path(path, stations_1)
    print(f"{stations_1[end]}: Distance = {d}, Path = {path_str}") # prints the distance and the path to the chosen stations 
