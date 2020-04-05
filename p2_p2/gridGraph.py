from graph import Graph
from node import Node


class GridGraph(Graph):
    def addNode(self, nodeVal, x, y):
        node = Node(nodeVal)
        node.coordinate.append(x)
        node.coordinate.append(y)
        self.nodes[node] = node
        return node

    def addUndirectedEdge(self, first: Node, second: Node):
        if (first.coordinate[0] == second.coordinate[0] + 1 and first.coordinate[1] == second.coordinate[1]) \
        or (first.coordinate[0] == second.coordinate[0] - 1 and first.coordinate[1] == second.coordinate[1])  \
        or (first.coordinate[0] == second.coordinate[0] and first.coordinate[1] == second.coordinate[1] + 1) \
        or (first.coordinate[0] == second.coordinate[0] and first.coordinate[1] == second.coordinate[1] - 1):
            super().addUndirectedEdge(first, second)
