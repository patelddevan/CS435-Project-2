from typing import Dict, List


class Node:
    def __init__(self, nodeVal):
        self.nodeVal: int = nodeVal
        self.neighbors: Dict[Node, int]  = {}
        self.coordinate: List[int] = []

    def getNodeVal(self):
        return self.nodeVal

    def getNeighbors(self):
        return self.neighbors

    def getCoordinate(self):
        return self.coordinate
