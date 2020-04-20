from graph import Graph
from node import Node


class WeightedGraph(Graph):
    def addWeightedEdge(self, first: Node, second: Node, edgeWeight: int):
        if first in self.nodes:
            self.nodes[first].neighbors[second] = edgeWeight
