class Graph:
  def __init__(self,num_of_vtx):#number of each row
   
    self.num_of_vtx=num_of_vtx
    self.adjMatrix= [[-1]*num_of_vtx for _ in self.num_of_vtx]#creates vertexes/nodes that all have the value -1 (2d array)
    self.vertices={} #dictionary for the vertices
    self.verticeslist =[-1]*num_of_vtx #creates an array based on the num of vertex


  def add_vertex(self,vtx_number,id):
    if 0 <= vtx_number <= self.num_of_vtx:#vtx_number is a index of vertex if
      self.vertices[id]=vtx_number #id becomes key vtx_number is the value
      self.verticeslist[vtx_number]=id#puts vtx_number key into the vertices list




  def add_edges(self,point1,point2,weight):

    point1 = self.vertices[point1] #point between vertex1
    point2=self.vertices[point2]#point between  vertex2
    self.adjMatrix[point1][point2]= weight

    #if this is a non Directed Adjacey graph
    self.adjMatrix[point2][point1]=weight

  
  def get_vertex(self):
    return self.verticeslist

  def print_matrix(self):
    for _ in self.adjMatrix:
      print(_)

  def get_edges(self):
    edges=[]
    for i in range(self.num_of_vtx):
      for j in range(self.num_of_vtx):
        if self.adjMatrix != -1:
          edges.append(self.verticeslist[i],self.verticeslist[j],self.adjMatrix[i][j])


  
