import math 

class Node:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight
    def __str__(self):
        return "<{},{}>".format(self.node,self.weight)

class Graph:
    def __init__(self,n_node):
        self.adjList = {}
        self.n_node = n_node
    def addNode(self,src,node):
        if src not in self.adjList:
            self.adjList[src] = []
        self.adjList[src].append(node)
    
    
    def dijkstra(self,start):
        distance = {}
        for i in self.adjList:
            distance[i] = math.inf
        distance[start] = 0
        min_vals = {start:0}
        while min_vals:
            source_node = min(min_vals,key = lambda k: min_vals[k])
            del min_vals[source_node]

            for adj_node in self.adjList[source_node]:
                adjNode = adj_node.node
                adjDist = adj_node.weight

                if distance[adjNode] > distance[source_node] + adjDist:
                    distance[adjNode]  =  distance[source_node] + adjDist
                    min_vals[adjNode] = distance[adjNode]
        for i in self.adjList:
            print("Source node: {} -> Destination Node: {} => Distance: {}".format(start,i,distance[i]))

g = Graph(6)
g.addNode('A', Node('B', 5))
g.addNode('A', Node('C', 1))
g.addNode('A', Node('D', 4))
g.addNode('B', Node('A', 5))
g.addNode('B', Node('C', 3))
g.addNode('B', Node('E', 8))
g.addNode('C', Node('A', 1))
g.addNode('C', Node('B', 3))
g.addNode('C', Node('D', 2))
g.addNode('C', Node('E', 1))
g.addNode('D', Node('A', 4))
g.addNode('D', Node('C', 2))
g.addNode('D', Node('E', 2))
g.addNode('D', Node('F', 1))
g.addNode('E', Node('B', 8))
g.addNode('E', Node('C', 1))
g.addNode('E', Node('D', 2))
g.addNode('E', Node('F', 3))
g.addNode('F', Node('D', 1))
g.addNode('F', Node('E', 3))
g.dijkstra('A')