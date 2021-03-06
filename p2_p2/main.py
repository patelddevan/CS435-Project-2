from collections import deque
from random import getrandbits, randint
from sys import maxsize
from typing import Dict, List, Set

from directedGraph import DirectedGraph
from graph import Graph
from graphSearch import GraphSearch
from gridGraph import GridGraph
from node import Node
from topSort import TopSort
from weightedGraph import WeightedGraph


def createRandomUnweightedGraphIter(n: int) -> Graph:
    graph = Graph()
    for i in range(n):
        graph.addNode(i)
    visited = set()
    for node in graph.nodes:
        for _node in graph.nodes:
            if _node not in visited and bool(getrandbits(1)):
                graph.addUndirectedEdge(node, _node)
        visited.add(node)
    return graph

# 3c
def createLinkedList(n: int) -> Graph:
    graph = Graph()
    if not n:
        return graph
    prev = graph.addNode(0)
    for i in range(1, n):
        curr = graph.addNode(i)
        graph.addUndirectedEdge(prev, curr)
        prev = curr
    return graph

def BFTRecLinkedList() -> List[Node]:
    graph = createLinkedList(100)
    return GraphSearch.BFTRec(graph)

def BFTIterLinkedList() -> List[Node]:
    graph = createLinkedList(10000)
    return GraphSearch.BFTIter(graph)

def createRandomDAGIter(n: int) -> DirectedGraph:
    graph = DirectedGraph()
    for i in range(n):
        graph.addNode(i)
    for node in graph.nodes:
        for _node in graph.nodes:
            if node is not _node and bool(getrandbits(1)):
                if not hasCycle(graph, node, _node):
                    graph.addDirectedEdge(node, _node)
    return graph

def hasCycle(graph: DirectedGraph, first: Node, second: Node) -> bool:
    grey = set()
    stack = deque()
    stack.append(first)
    isFirst = True
    while len(stack) != 0:
        next = stack.pop()
        grey.add(next)
        for neighbor in next.getNeighbors():
            if neighbor in grey:
                return True
            stack.append(neighbor)
        if isFirst:
            isFirst = False
            stack.append(second)
    return False

def createRandomCompleteWeightedGraph(n: int) -> WeightedGraph:
    graph = WeightedGraph()
    for i in range(n):
        graph.addNode(i)
    nodes = graph.getAllNodes()
    for node in nodes:
        for _node in nodes:
            if node is not _node:
                graph.addWeightedEdge(node, _node, randint(0, 2000))
    return graph 

# 5d
def _createLinkedList(n: int) -> WeightedGraph:
    graph = WeightedGraph()
    if not n:
        return Graph
    prev = graph.addNode(0)
    for i in range(1, n):
        curr = graph.addNode(i)
        graph.addWeightedEdge(prev, curr, randint(0, 2000))
        prev = curr
    return graph

def dijkstras(start: Node) -> Dict:
    distance = {}
    distance[start] = 0
    visited = set()
    curr = start
    while curr is not None and curr in distance:
        visited.add(curr)
        for neighbor in curr.getNeighbors():
            if neighbor not in visited:
                if (neighbor not in distance) or (distance[curr] + curr.getNeighbors()[neighbor] < distance[neighbor]):
                    distance[neighbor] = distance[curr] + curr.getNeighbors()[neighbor]
        curr = getCurrent(distance, None, visited, curr.getNeighbors())
    print("# of nodes finalized in dijkstras", len(visited))
    return distance

def createRandomGridGraph(n: int) -> GridGraph:
    graph = GridGraph()
    nodeValue = 0
    for i in range(n):
        for j in range(n):
            graph.addNode(nodeValue, i, j)
            nodeValue += 1
    nodes = graph.getAllNodes()
    visited = set()
    for node in nodes:
        visited.add(node)
        for _node in nodes:
            if _node not in visited and bool(getrandbits(1)):
                graph.addUndirectedEdge(node, _node)
    return graph

def astar(sourceNode: Node, destNode: Node) -> List[Node]:
    parent = {}
    distance = {}
    heuristic = {}
    distance[sourceNode] = 0
    heuristic[sourceNode] = manhattanDistance(sourceNode, destNode)
    visited = set()
    curr = sourceNode
    while curr is not destNode:
        visited.add(curr)
        for neighbor in curr.getNeighbors():
            if neighbor not in visited and (neighbor not in distance or distance[neighbor] < distance[curr]):
                distance[neighbor] = distance[curr] + 1
                heuristic[neighbor] = manhattanDistance(neighbor, destNode)
        p = curr
        curr = getCurrent(distance, heuristic, visited, curr.getNeighbors())
        if curr is None:
            break
        parent[curr] = p
    print("# of nodes finalized in astar", len(visited))
    c = destNode
    path = []
    while c is not None:
        path.append(c)
        if c in parent:
            c = parent[c]
        else:
            c = None
    path.reverse()
    if path[0] is sourceNode and path[-1] is destNode:
        return path

def manhattanDistance(src: Node, dst: Node) -> int:
    return abs(dst.getCoordinate()[0] - src.getCoordinate()[0]) + abs(dst.getCoordinate()[1] - src.getCoordinate()[1])

def getCurrent(distance: Dict, heuristic: Dict, visited: Set[Node], neighbors: List[Node]):
    min = maxsize
    minKey = None
    if heuristic is None:
        for i in neighbors:
            if i not in visited and distance[i] < min:
                min = distance[i]
                minKey = i
    else:
        for i in neighbors:
            if i not in visited and distance[i] + heuristic[i] < min:
                min = distance[i] + heuristic[i]
                minKey = i
    return minKey

verbose = False

def main():
    graph = createRandomUnweightedGraphIter(10)
    nodes = graph.getAllNodes()
    listOfNodes = list(nodes)
    listOfNodes.sort(key=lambda x: x.nodeVal)
    dfs_rec_arr = GraphSearch.DFSRec(listOfNodes[3], listOfNodes[9])
    dfs_iter_arr = GraphSearch.DFSIter(listOfNodes[3], listOfNodes[9])
    bft_rec_arr = GraphSearch.BFTRec(graph)
    bft_iter_arr = GraphSearch.BFTIter(graph)
    print("--- Random Unweighted Graph ---")
    printGraph(graph)
    print("--- DFS-Rec ---")
    printList(dfs_rec_arr)
    print("\n--- DFS-Iter ---")
    printList(dfs_iter_arr)
    print("\n--- BFT-Rec ---")
    printList(bft_rec_arr)
    print("\n--- BFT-Iter ---")
    printList(bft_iter_arr)

    _graph = createLinkedList(10)
    _nodes = _graph.getAllNodes()
    _listOfNodes = list(_nodes)
    _listOfNodes.sort(key=lambda x: x.nodeVal)
    _dfs_rec_arr = GraphSearch.DFSRec(_listOfNodes[3], _listOfNodes[9])
    _dfs_iter_arr = GraphSearch.DFSIter(_listOfNodes[3], _listOfNodes[9])
    _bft_rec_arr = GraphSearch.BFTRec(_graph)
    _bft_iter_arr = GraphSearch.BFTIter(_graph)
    print("\n--- Linked List ---")
    printGraph(_graph)
    print("--- DFS-Rec ---")
    printList(_dfs_rec_arr)
    print("\n--- DFS-Iter ---")
    printList(_dfs_iter_arr)
    print("\n--- BFT-Rec ---")
    printList(_bft_rec_arr)
    print("\n--- BFT-Iter ---")
    printList(_bft_iter_arr)

    topSort_graph = createRandomDAGIter(1000)
    print("\n--- Random Directed Acyclic Graph ---")
    printGraph(topSort_graph)
    topSort_kahns = TopSort.Kahns(topSort_graph)
    print("--- Kahns Output---")
    printList(topSort_kahns)
    topSort_mDFS = TopSort.mDFS(topSort_graph)
    print("\n--- mDFS Output ---")
    printList(topSort_mDFS)

    dijkstras_graph = createRandomCompleteWeightedGraph(1000)
    print("\n--- Random Complete Weighted Graph ---")
    printGraph(dijkstras_graph)
    dijkstras_result = runDijkstras(dijkstras_graph, 2)
    print("--- Dijkstras Output ---")
    printDijkstras(dijkstras_result)

    astar_graph = createRandomGridGraph(100)
    print("--- Random Grid Graph ---")
    printGraph(astar_graph)
    astar_result = runAstar(astar_graph, 0, 9999)
    print("--- A* Output ---")
    printList(astar_result)

def printGraph(graph: DirectedGraph):
    if verbose:
        print("Start to Print Graph")
        nodes = graph.getAllNodes()
        for node in nodes:
            print("--- Node", node.getNodeVal(), "---")
            for neighbor in node.getNeighbors():
                print("Neighbor -", neighbor.getNodeVal(), "Weight -", node.getNeighbors()[neighbor])
        print("Done Printing Graph")

def printDijkstras(result: Dict):
    print("To:Cost")
    if result:
        for i in result:
            print(i.getNodeVal(), result[i], sep=":")
    else:
        print(result)

def runDijkstras(graph: WeightedGraph, start: int) -> Dict:
    print("--- Dijkstras From Node", start, "---")
    nodes = graph.getAllNodes()
    list_of_nodes = list(nodes)
    list_of_nodes.sort(key=lambda x: x.nodeVal)
    return dijkstras(list_of_nodes[start])

def runAstar(graph: GridGraph, start: int, end: int) -> List[Node]:
    print("--- A* From Node", start, "to", end, "---")
    nodes = graph.getAllNodes()
    list_of_nodes = list(nodes)
    list_of_nodes.sort(key=lambda x: x.nodeVal)
    return astar(list_of_nodes[start], list_of_nodes[end])

def printList(result: List[Node]):
    if result:
        for i in result:
            print(i.getNodeVal(), end=' ')
    else:
        print(result)

if __name__ == "__main__":
    main()
