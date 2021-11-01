from queue import LifoQueue
from newGraph import Graph
from queue import Queue

nodes=["A","B","C","D","E","F"]
connects=[('A', 'B'), ('A', 'C'), ('D', 'E'), ('B', 'D'), ('B', 'E')]

graph=Graph(nodes,False,connects)
graph.print_adj_list()

visited={}
level={}
parent={}
dfs_traversal_output=[]
stack=LifoQueue()

for node in graph.adj_list:
 
    
    visited[node]=False
    level[node]=0 #could be any number but for the sake of it we do -1
    parent[node]=None



def dfs(visited,graph,node):
    if not visited[node]:
        visited[node]=True
        dfs_traversal_output.append(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
        

dfs(visited,graph.adj_list,"A")

print(dfs_traversal_output)



