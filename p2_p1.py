import random

class Graph:
    def __init__(self):
        self.adjList = {}

    def addNode(self, nodeVal):
        self.adjList[nodeVal] = []
    
    def addUndirectedEdge(self, first, second):
        self.adjList[first].append(second)
        if first != second:
            self.adjList[second].append(first)
    
    def removeUndirectedEdge(self, first, second):
        self.adjList[first].remove(second)
        if first != second:
            self.adjList[second].remove(first)
    
    def getAllNodes(self):
        return set(self.adjList)

class Main:
    @staticmethod
    def createRandomUnweightedGraphIter(n):
        graph = Graph()
        for i in range(n):
            graph.addNode(i)
        visited = set()
        for node in graph.adjList:
            for _node in graph.adjList: 
                if _node not in visited and bool(random.getrandbits(1)):
                    graph.addUndirectedEdge(node, _node)
            visited.add(node)
        return graph

    @staticmethod
    def createLinkedList(n):
        graph = Graph()
        if not n: 
            return graph
        graph.addNode(0)
        for i in range(1, n):
            graph.addNode(i)
            graph.addUndirectedEdge(i - 1, i)
        return graph

    @staticmethod
    def BFTRecLinkedList():
        graph = Main.createLinkedList(100)
        return GraphSearch.BFTRec(graph)
    
    @staticmethod
    def BFTIterLinkedList():
        graph = Main.createLinkedList(10000)
        return GraphSearch.BFTIter(graph)

class GraphSearch:
    @staticmethod
    def DFSRec(graph, start, end):
        arr = []
        visited = set()
        return GraphSearch.DFSRecHelper(graph, start, end, arr, visited)

    @staticmethod
    def DFSRecHelper(graph, start, end, arr, visited):
        arr.append(start)
        visited.add(start)
        if start == end:
            return 1
        neighbors = graph.adjList[start]
        for neighbor in neighbors:
            if neighbor not in visited:
                result = GraphSearch.DFSRecHelper(graph, neighbor, end, arr, visited)
                if result is not None:
                    return arr
        return None

    @staticmethod
    def DFSIter(graph, start, end):
        arr = []
        visited = set()
        stack = [start]
        while len(stack) != 0:
            next = stack.pop()
            arr.append(next)
            visited.add(next)
            if next == end:
                return arr
            neighbors = graph.adjList[next]
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)

    @staticmethod
    def BFTRec(graph):
        arr = []
        visited = set()
        for node in graph.adjList:
            if node not in visited:
                GraphSearch.BFTRecHelper(graph, [node], arr, visited)
        return arr

    @staticmethod
    def BFTRecHelper(graph, queue, arr, visited):
        if len(queue) != 0:
            next = queue.pop(0)
            arr.append(next)
            visited.add(next)
            neighbors = graph.adjList[next]
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
            return GraphSearch.BFTRecHelper(graph, queue, arr, visited)

    @staticmethod
    def BFTIter(graph):
        arr = []
        visited = set()
        for node in graph.adjList:
            if node not in visited:
                GraphSearch.BFTIterHelper(graph, [node], arr, visited)
        return arr

    @staticmethod
    def BFTIterHelper(graph, queue, arr, visited):
        while len(queue) != 0:
            next = queue.pop(0)
            arr.append(next)
            visited.add(next)
            neighbors = graph.adjList[next]
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

def main(): 
    graph = Main.createRandomUnweightedGraphIter(10)
    dfs_rec_arr = GraphSearch.DFSRec(graph, 3, 9)
    dfs_iter_arr = GraphSearch.DFSIter(graph, 3, 9)
    bft_rec_arr = GraphSearch.BFTRec(graph)
    bft_iter_arr = GraphSearch.BFTIter(graph)
    print("--- Random Unweighted Graph ---")
    print("DFS-Rec ", dfs_rec_arr)
    print("DFS-Iter", dfs_iter_arr)
    print("BFT-Rec ", bft_rec_arr)
    print("BFT-Iter", bft_iter_arr)

    _graph = Main.createLinkedList(10)
    _dfs_rec_arr = GraphSearch.DFSRec(_graph, 3, 9)
    _dfs_iter_arr = GraphSearch.DFSIter(_graph, 3, 9)
    _bft_rec_arr = GraphSearch.BFTRec(_graph)
    _bft_iter_arr = GraphSearch.BFTIter(_graph)
    print("--- Linked List ---")
    print("DFS-Rec ", _dfs_rec_arr)
    print("DFS-Iter", _dfs_iter_arr)
    print("BFT-Rec ", _bft_rec_arr)
    print("BFT-Iter", _bft_iter_arr)

    print("--- BFT-Iter Linked List ---")
    print(Main.BFTIterLinkedList())
    print("--- BFT-Rec Linked List ---")
    print(Main.BFTRecLinkedList())

if __name__ == "__main__":
    main()
