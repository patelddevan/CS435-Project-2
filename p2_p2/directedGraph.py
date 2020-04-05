from typing import Set

from node import Node


class DirectedGraph:
    def __init__(self):
        self.nodes = {}

    def addNode(self, nodeVal: int):
        node = Node(nodeVal)
        self.nodes[node] = node
        return node

    def addDirectedEdge(self, first: Node, second: Node):
        self.nodes[first].neighbors[second] = 0
    
    def removeDirectedEdge(self, first: Node, second: Node):
        self.nodes[first].neighbors.pop(second, None)
    
    def getAllNodes(self) -> Set[Node]:
        return set(self.nodes)
