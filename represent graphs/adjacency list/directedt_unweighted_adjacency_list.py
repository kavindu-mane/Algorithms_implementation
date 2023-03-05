class Node:
    def __init__(self, value ):
        self.value = value
        self.next = None

class Graph:
    def __init__(self):
        self.graphs = {}
        self.inverse_graphs = {}

    def add_edge(self , start , end):
       
       graphs = self.graphs
       inverse_graphs = self.inverse_graphs

       if end not in inverse_graphs.keys():
           inverse_graphs[end] = None

       node = Node(start)
       node.next = inverse_graphs[end]
       inverse_graphs[end] = node

       if start not in graphs.keys():
           graphs[start] = None

       node = Node(end)
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
                    print(" --> {}".format(temp.value) , end = " ")
                    temp = temp.next
                print()

graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "D")
graph.add_edge("B", "C")
graph.add_edge("E", "C")
graph.add_edge("E", "F")
graph.add_edge("F", "A")

graph.print_result()