from graph import Graph
from node import Node


class WeightedGraph(Graph):
    def addWeightedEdge(self, first: Node, second: Node, edgeWeight: int):
        self.nodes[first].neighbors[second] = edgeWeight
