class Graph:
    def __init__(self,adjList=None):
        if(adjList == None):
            adjList = {}
        self.adjList = adjList
    def __str__(self):
        string = ''
        for j in self.adjList:
            string = string+str(j)+':\t'+str(self.adjList[j])+'\n'
        return string
    def addEdge(self,pair_tuple):
        self.adjList[pair_tuple[0]].append(pair_tuple[1])
        self.adjList[pair_tuple[1]].append(pair_tuple[0])
    def addVertex(self,new_vertex):
        self.adjList[new_vertex] = []
    def removeVertex(self,vertex):
        for j in self.adjList:
            if vertex in self.adjList[j]:
                self.adjList[j].remove(vertex)
        self.adjList.pop(vertex)
    def removeEdge(self,pair):
        self.adjList[pair[0]].remove(pair[1])
        self.adjList[pair[1]].remove(pair[0])
    def topSortUtil(self,v,visited,stack):
        visited.append(v)
        for i in self.adjList[v]:
            if i not in visited:
                self.topSortUtil(i,visited,stack)
        stack.insert(0,v)
    def TopogologicalSorting(self):
        stack = []
        visited = []
        for i in list(self.adjList):
            if i not in visited:
                self.topSortUtil(i,visited,stack)
            
        return stack
            
myDict = {'A':['C'],
           'B':['C','D'],
           'C':['E'],
           'D':['F'],
           'E':['H','F'],
           'F':['G'],
           'G':[],
           'H':[] }
my_graph = Graph(myDict)
# print(my_graph)

stack =  my_graph.TopogologicalSorting()
print(stack)