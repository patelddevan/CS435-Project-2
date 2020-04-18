from collections import deque
from typing import Dict, List, Set

from directedGraph import DirectedGraph
from node import Node


class TopSort:
    @staticmethod
    def Kahns(graph: DirectedGraph) -> List[Node]:
        nodes = graph.getAllNodes()
        inDegreeMap = {node:0 for node in nodes}
        for node in nodes:
            for neighbor in node.neighbors:
                inDegreeMap[neighbor] += 1
        topSort = []
        queue = deque()
        for node in inDegreeMap:
            if inDegreeMap[node] == 0:
                queue.append(node)
        count = 0
        while len(queue) != 0:
            node = queue.popleft()
            topSort.append(node)
            count += 1
            for neighbor in node.neighbors:
                inDegreeMap[neighbor] -= 1
                if inDegreeMap[neighbor] == 0:
                    queue.append(neighbor)
        if count != len(graph.nodes):
            return None
        return topSort

    @staticmethod
    def mDFS(graph: DirectedGraph) -> List[Node]:
        stack = []
        visited = set()
        for node in graph.getAllNodes():
            if node not in visited:
                TopSort.mDFSHelper(graph, node, stack, visited)
        stack.reverse()
        return stack
    
    @staticmethod
    def mDFSHelper(graph: DirectedGraph, node: Node, stack: List[Node], visited: Set[Node]):
        visited.add(node)
        for neighbor in node.neighbors:
            if neighbor not in visited:
                TopSort.mDFSHelper(graph, neighbor, stack, visited)
        stack.append(node)
