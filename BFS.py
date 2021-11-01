from newGraph import Graph
from queue import Queue

nodes=["A","B","C","D","E","F"]
connects=[('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C'),('C','B')]

graph=Graph(nodes,False,connects)
graph.print_adj_list()

visited={}
level={}
parent={}
bfs_traversal_output=[]
queue=Queue()

""" sets all values to false none and minus to represent graph hasnt been traversed """
for node in graph.adj_list:
    visited[node]=False
    parent[node]=None
    level[node]=-1


source_node="A"
visited[source_node]=True
level[source_node]=0
queue.put(source_node)

while not queue.empty():
    node_on_queue=queue.get() #get the node on the queue
    bfs_traversal_output.append(node_on_queue) #put that node onto a traversed array

    for node in graph.adj_list[node_on_queue]:#loop based on how many edges a node has
        if not visited[node]:
            visited[node]=True
            parent[node]=node_on_queue
            level[node]=level[node_on_queue]+1
            queue.put(node)


print(bfs_traversal_output)
print(parent)
print(level)
print(visited)