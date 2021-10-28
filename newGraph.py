class Graph:
    def __init__(self,*args):
        self.nodes=args[0]#wil be an array of nodes
        self.directed=args[1]
        self.adj_list={}
        self.set_nodes_empty()


        if len(args)==3:
            
            self.add_connections(args[2])


    def add_connections(self,connections):
        for node1,node2 in connections:
            self.add_edge(node1,node2)

        



    def set_nodes_empty(self):
        for node in self.nodes:
            self.adj_list[node]=[]# sets all nodes to have no edges

    def add_edge(self,node1,node2):
        if node2 not in self.adj_list[node1]:
            self.adj_list[node1].append(node2)
            if not self.directed:
                self.adj_list[node2].append(node1)

    def print_adj_list(self):
        for node in self.adj_list:
            print(node,':',self.adj_list[node])
            

      


if __name__=="__main__":

    nodes=["A","B","C","D","E","F"]

    connects=[('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C'),('C','B')]

    graph=Graph(nodes,False,connects)

    graph.print_adj_list()