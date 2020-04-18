from collections import deque
from typing import List, Set

from graph import Graph
from node import Node


class GraphSearch:
    @staticmethod
    def DFSRec(start: Node, end: Node):
        arr = []
        visited = set()
        return GraphSearch.__DFSRecHelper(start, end, arr, visited)

    @staticmethod
    def __DFSRecHelper(start: Node, end: Node, arr: List[Node], visited: Set[Node]):
        arr.append(start)
        visited.add(start)
        if start == end:
            return 1
        for neighbor in start.neighbors:
            if neighbor not in visited:
                result = GraphSearch.__DFSRecHelper(neighbor, end, arr, visited)
                if result:
                    return arr

    @staticmethod
    def DFSIter(start: Node, end: Node) -> List[Node]:
        arr = []
        visited = set()
        stack = deque()
        stack.append(start)
        while len(stack) != 0:
            next = stack.pop()
            arr.append(next)
            visited.add(next)
            if next == end:
                return arr
            for neighbor in next.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

    @staticmethod
    def BFTRec(graph: Graph) -> List[Node]:
        arr = []
        visited = set()
        for node in graph.getAllNodes():
            if node not in visited:
                queue = deque()
                queue.append(node)
                GraphSearch.__BFTRecHelper(graph, queue, arr, visited)
        return arr

    @staticmethod
    def __BFTRecHelper(graph: Graph, queue: deque, arr: List[Node], visited: Set[Node]):
        if len(queue) != 0:
            next = queue.popleft()
            arr.append(next)
            visited.add(next)
            for neighbor in next.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
            return GraphSearch.__BFTRecHelper(graph, queue, arr, visited)

    @staticmethod
    def BFTIter(graph: Graph) -> List[Node]:
        arr = []
        visited = set()
        for node in graph.getAllNodes():
            if node not in visited:
                queue = deque()
                queue.append(node)
                GraphSearch.__BFTIterHelper(graph, queue, arr, visited)
        return arr
    
    @staticmethod
    def __BFTIterHelper(graph: Graph, queue: deque, arr: List[Node], visited: Set[Node]):
        while len(queue) != 0:
            next = queue.popleft()
            arr.append(next)
            visited.add(next)
            for neighbor in next.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
