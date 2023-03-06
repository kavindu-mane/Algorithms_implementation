class Node:
    def __init__(self, value , weight):
        self.value = value
        self.weight = weight
        self.next = None

class Graph:
    def __init__(self):
        self.graphs = {}
        self.inverse_graphs = {}

    def add_edge(self , start , end , weight):
       
       graphs = self.graphs
       inverse_graphs = self.inverse_graphs

       if end not in inverse_graphs.keys():
           inverse_graphs[end] = None

       node = Node(start ,weight)
       node.next = inverse_graphs[end]
       inverse_graphs[end] = node

       if start not in graphs.keys():
           graphs[start] = None

       node = Node(end ,weight)
       node.next = graphs[start]
       graphs[start] = node

    def print_result(self):

        for i in range(2):
            graphs = None

            if i == 0:
                graphs = self.graphs
                print("Adjacent List : ")
            else:
                graphs = self.inverse_graphs
                print("\nInverse Adjacent List : ")
            
            graphs = dict(sorted(graphs.items()))
            
            for key in graphs.keys():
                print("{} : ".format(key) ,end = "")
                temp = graphs[key]
                while temp:
                    print(" --> {} ({})".format(temp.value , temp.weight) , end = " ")
                    temp = temp.next
                print()

graph = Graph()
graph.add_edge("A", "B" , 2)
graph.add_edge("A", "C" , 5)
graph.add_edge("A", "D" , 8)
graph.add_edge("B", "C" , 9)
graph.add_edge("E", "C" , 1)
graph.add_edge("E", "F" , 7)
graph.add_edge("F", "A" , 4)

graph.print_result()