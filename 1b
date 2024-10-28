from Func_CW.generate_random_graph import generate_random_graph # FROM THE COURSEWORK GIVEN LIBRARY
import random
class GenerateGraph:
    def __innit__(self):
        self.graph = None # represents the graph 


    def graph_generator(self, v, edge_prob, by_list, directed, weighted, min_weight, max_weight):
        """
        Creates a random graph based on the parameters specified.
        Arguments: 
        
        v(int), the number of vertices in the graph
        edge_prob(num) the probability of one vertex to have an edge with another vertex
        by_list(bool): True if graph to be in adjacency list, false if for matrix form
        directed(bool): True for graph to be directed, false otherwise
        weighted(bool): True for the graph to be weighted, false otherwise
        min_weight(int): What is the minimum weight of the graph, if any
        max_weight(int): What is the maximum weight for an edge, if any
        """

        #parameters validation check
        if (weighted == True) and (min_weight > max_weight):
            raise ValueError("min_weight cannot be larger than max_weight")

        if type(v) != int:
            raise ValueError("V needs to be an integer")
        if type(edge_prob) != float and type(edge_prob) != int:
            raise ValueError("edge_prob needs to be either int or float")

        if type(weighted) != bool or type(directed) != bool:
            raise ValueError("weighted and directed need to be bool values")

        # if validations pass
        else: 
            self.graph = generate_random_graph(v, edge_prob, by_list, directed, weighted, min_weight, max_weight) # create the graph with the generate random graph algorithm
            return self.graph

#testing 
if __name__ == '__main__':
    generate_graph = GenerateGraph()
    generated_graph = generate_graph.graph_generator(random.randint(0, 20), 0.15,True, False, True, 2, 15)
    print(generated_graph.get_card_E())
    print(generated_graph.get_edge_list())
