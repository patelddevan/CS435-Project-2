from typing import Dict, List


class Node:
    def __init__(self, nodeVal):
        self.nodeVal: int = nodeVal
        self.neighbors: Dict[Node: int]  = {}
        self.coordinate: List[int] = []
