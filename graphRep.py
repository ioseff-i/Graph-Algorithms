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
    def bfs_traversal(self,vertex):
        queue = [vertex]
        visited = [vertex]
        while queue:
            dequeue = queue.pop(0)
            print(dequeue)
            for adjacent in self.adjList[dequeue]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    queue.append(adjacent)
                    
    def dfs_traversal(self,vertex):
        stack = [vertex]
        visited = [vertex]
        while stack:
            dequeue = stack.pop()
            print(dequeue,end=' ')
            for adjacent in self.adjList[dequeue]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    stack.append(adjacent)
                    
                
            
            
myDict = {'A':['B','C'],
           'B':['A','D'],
           'C':['A','E'],
           'D':['B','F'],
           'E':['C','F'],
           'F':['D','E'] }
my_graph = Graph(myDict)
# my_graph.removeVertex(5)
my_graph.bfs_traversal('A')

# my_graph.addEdge('E','F')
# my_graph.bfs_traversal('A')
# print('\n\n\n')
# my_graph.dfs_traversal('A')
