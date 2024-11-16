# adjacency lists for graphs
# written algorithm for creating the graph 
# then writing the algorithm
#imports 
from Func_CW.adjacency_list_graph import AdjacencyListGraph# data structure for storing the graph
from Func_CW.mst import kruskal
import pandas # used to read the excel  file
# creating the graph

class Graph_From_CSV:
    def __init__(self, csv_file):
        """
        Creates a graph from the coursework csv file given to us
        Parameters: csv_file (path to the csv file)
        """
        self.excel_file = csv_file # csv file path stored here
        self.graph = None # variable contains the adjacency list which holds the graph
        self.station_list = None # A variable containing the names of all the stations in the graph 
        self.lines_list = None # A variable containing all the lines between stations, and their time (weight)

    def _extract_stations(self):
        """
        Method to create the graph from the csv file linked in the coursework

        Returns: station_list(list)
                lines_list(list)
        """
        station_set = set() # set which will hold the names of the stations (which represent the nodes)
        self.station_list = [] # a list containing and indexing the stations in the excel file
        file = pandas.read_excel(self.excel_file) # opens the file using pandas for it to be read
        stations_from_excel_file = file[file[['Station Name 2', 'Time']].isna().any(axis=1)] # isolates only rows which have station names 2 and the time as null
        for index, row in stations_from_excel_file.iterrows(): # adding all station names to the station set and station list from the excel file
            if row['Station Name 1'] not in station_set:
                station_set.add(row['Station Name 1']) # add the name of the station to the set
                self.station_list.append(row['Station Name 1']) # adds the name of the station to the list


        self.lines_list = [] # list will contain lines between stations, which will be edges in the graph
        lines_from_excel_file = file[file[['Station Name 2', 'Time']].notna().any(axis=1)] # now isolating rows which have all collumns as not null
        for index, row in lines_from_excel_file.iterrows(): # for each row
            self.lines_list.append([row['Station Name 1'], row['Station Name 2'], row['Time']]) # append a list to the lines list containing the station names and the times between them

        return True

    def create_graph(self, weighted=True, directed=False):
        """
        Creates a graph from the excel file using adjacency list structure

        Parameters: weighted(bool): whether the edges of the graph are weighted or not
                    directed(bool): whether the edges of the graph will have a direction
        """

        self._extract_stations()  # extract the stations and lines from the excel vile

        self.graph = AdjacencyListGraph(len(self.station_list), directed=False, weighted=True) # create an adjacency list graph, with the direction disabled and weights enabled

        for i in self.lines_list: # for each line
            try:
                self.graph.insert_edge(self.station_list.index(i[0]), self.station_list.index(i[1]), i[2]) # insert the edge, using the indexes of stations at the station_list algorithm as the number for the station
            except RuntimeError: # if there are any Runtime exceptions raised because of 2 stations already being connected
                continue  #ignore and continue the loop
        return # once complete, return 

class ClosedRoutes:
    def __init__(self, graph, station_list):
        """
        Desc: Responsible for searching whether closure of routes is feasible

        Parameters: graph(adjacency list or matrix))
                    station_list(list), a list containing all of the station names which are also indexed. Not mandatory unless user wants stations to be named

        """
        self.graph = graph # the graph of the underground
        self.station_list = station_list # the graph containing the names of stations

    
    def find_what_routes_to_close(self, named_list):
        """
        Desc: Uses kruskal algorithm to find the minimal spanning tree of the underground network. Then, it isolates edges not part of that mst
        and returns them as lines to close

        Parameters: graph(adjacency list/matrix of a graph) 
                    named_list(bool), asks whether to also return a named list of the edges

        Returns: list_of_closed_stations (list)

        Assumptions: That the graph parameter provided is an adjacency list
        """

        if type(named_list) != bool:
            raise ValueError("named_list must be value type bool")

        all_edges = set() # set of all edges
        mst_edges = set() # set of mst edges

        all_edges.update(self.graph.get_edge_list()) # adding all edges to the first set

        mst = kruskal(self.graph) # minimal spanning tree

        mst_edges.update(mst.get_edge_list()) 
        all_edges -= mst_edges

        if named_list == True:
            return all_edges, self._named_lines(all_edges)

        else:
            return all_edges

    def _named_lines(self, edges):
        """
        Returns a list of edges, however with the vertices named,  as adjacency list graphs do not support naming of vertices/nodes

        Parameters: edges(set), a set of tuples

        Returns: List of named stations

        Assuming: edges gives are sets which contain tuples
        """

        if type(edges) != set: # parameter checker 1
            raise ValueError("Parameter given must be a set")
        
        if type(next(iter(edges))) != tuple: # parameter checker 2
            raise ValueError("Elemenets of the edges set must be tuples")
    
        named_list = [] # named list containing names edges
        edge_list = list(edges) # converts edge to list for easier iterations
        for i in edge_list: # for each edge in the list
            named_list.append(["{} -- {}".format(self.station_list[i[0]], self.station_list[i[1]])])
        
        return named_list


if __name__ == "__main__":
    graph = Graph_From_CSV('London Underground data.xlsx')
    graph.create_graph()
    closed_stations = ClosedRoutes(graph.graph, graph.station_list)
    closed_stations_set, lines_named =closed_stations.find_what_routes_to_close(True)
    print(closed_stations_set)
    print(lines_named)
    
