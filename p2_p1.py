import random

class Graph:
    def __init__(self):
        self.adjList = dict()

    def addNode(self, nodeVal):
        self.adjList[nodeVal] = set()
    
    def addUndirectedEdge(self, first, second):
        self.adjList[first].add(second)
        if first != second:
            self.adjList[second].add(first)
    
    def removeUndirectedEdge(self, first, second):
        self.adjList[first].remove(second)
        if first != second:
            self.adjList[second].remove(first)
    
    def getAllNodes(self):
        return set(self.adjList)

    def addDirectedEdge(self, first, second):
        self.adjList[first].add(second)

class Main:
    @staticmethod
    def createRandomUnweightedGraphIter(n):
        graph = Graph()
        for i in range(n):
            graph.addNode(i)
        for node in graph.adjList:
            for _node in graph.adjList:
                if bool(random.getrandbits(1)):
                    graph.addUndirectedEdge(node, _node)
        return graph

    @staticmethod
    def createLinkedList(n):
        graph = Graph()
        if not n: 
            return graph
        graph.addNode(0)
        for i in range(1, n):
            graph.addNode(i)
            graph.addDirectedEdge(i - 1, i)
        return graph

class GraphSearch:
    @staticmethod
    def DFSRec(start, end):
        pass


def main():
    graph = Main.createRandomUnweightedGraphIter(10)
    nodes = graph.getAllNodes()
    for n in nodes:
        print(n)


if __name__ == "__main__":
    main()