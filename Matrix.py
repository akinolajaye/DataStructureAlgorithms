import random


class Graph:
  def __init__(self,nums):#vertexs
    nums.sort()
    self.nums=nums
    self.numvertex=len(nums)
    self.adjMatrix= [[-1]*self.numvertex for _ in range(self.numvertex)]#populate with -1s
    self.vertices={}
   
  def populate_sum(self):
    #edges=[]
    for i,val1 in enumerate(self.nums):
      for j,val2 in enumerate(self.nums):
        self.adjMatrix[i][j]=val1+val2
        
        #edges.append(self.verticeslist[i],self.verticeslist[j],self.adjMatrix[i][j])


  def print_matrix(self):
    for _ in self.adjMatrix:
      print(_)

    


  def add_edges(self,fro,to,weight):

    fro = self.vertices[fro] #point between vertex1
    to=self.vertices[to]#point between  vertex2
    self.adjMatrix[fro][to]= weight

    #if this is a non Directed Adjacey graph
    self.adjMatrix[to][fro]=weight

          
