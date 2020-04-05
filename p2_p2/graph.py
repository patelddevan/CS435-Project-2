from directedGraph import DirectedGraph
from node import Node


class Graph(DirectedGraph):
    def addUndirectedEdge(self, first: Node, second: Node):
        self.addDirectedEdge(first, second)
        if first is not second:
            self.addDirectedEdge(second, first)
    
    def removeUndirectedEdge(self, first: Node, second: Node):
        self.removeDirectedEdge(first, second)
        self.removeDirectedEdge(second, first)
