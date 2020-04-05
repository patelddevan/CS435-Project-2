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
        return Graph
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
        for neighbor in next.neighbors:
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
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                if (neighbor not in distance) or (distance[curr] + curr.neighbors[neighbor] < distance[neighbor]):
                    distance[neighbor] = distance[curr] + curr.neighbors[neighbor]
        curr = getCurrent(distance, None, visited, curr.neighbors)
    print("# of nodes finalized in dijkstras", len(visited))
    return distance

def createRandomGridGraph(n: int) -> GridGraph:
    graph = GridGraph()
    nodeValues = iter([i for i in range(n*n)])
    for i in range(n):
        for j in range(n):
            graph.addNode(next(nodeValues), i, j)
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
        for neighbor in curr.neighbors:
            if neighbor not in visited and (neighbor not in distance or distance[neighbor] < distance[curr]):
                distance[neighbor] = distance[curr] + 1
                heuristic[neighbor] = manhattanDistance(neighbor, destNode)
        p = curr
        curr = getCurrent(distance, heuristic, visited, curr.neighbors)
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
    if path[0] is not destNode or path[-1] is not sourceNode:
        return None
    path.reverse()
    return path

def manhattanDistance(src: Node, dst: Node) -> int:
    return abs(dst.coordinate[0] - src.coordinate[0]) + abs(dst.coordinate[1] - src.coordinate[1])

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
    print("--- DFS-Rec ---")
    if dfs_rec_arr is None: 
        print("None")
    else:
        for i in dfs_rec_arr: 
            print(i.nodeVal, end=' ')
    print("\n--- DFS-Iter ---")
    if dfs_iter_arr is None: 
        print("None")
    else:
        for i in dfs_iter_arr: 
            print(i.nodeVal, end=' ')
    print("\n--- BFT-Rec ---")
    if bft_rec_arr is None: 
        print("None")
    else:
        for i in bft_rec_arr: 
            print(i.nodeVal, end=' ')
    print("\n--- BFT-Iter ---")
    if bft_iter_arr is None:
        print("None")
    else:
        for i in bft_iter_arr: 
            print(i.nodeVal, end=' ')

    _graph = createLinkedList(10)
    _nodes = _graph.getAllNodes()
    _listOfNodes = list(_nodes)
    _listOfNodes.sort(key=lambda x: x.nodeVal)
    _dfs_rec_arr = GraphSearch.DFSRec(_listOfNodes[3], _listOfNodes[9])
    _dfs_iter_arr = GraphSearch.DFSIter(_listOfNodes[3], _listOfNodes[9])
    _bft_rec_arr = GraphSearch.BFTRec(_graph)
    _bft_iter_arr = GraphSearch.BFTIter(_graph)
    print("\n--- Linked List ---")
    print("--- DFS-Rec ---")
    if _dfs_rec_arr is None: 
        print("None")
    else:
        for i in _dfs_rec_arr: 
            print(i.nodeVal, end=' ')
    print("\n--- DFS-Iter ---")
    if _dfs_iter_arr is None: 
        print("None")
    else:
        for i in _dfs_iter_arr: 
            print(i.nodeVal, end= ' ')
    print("\n--- BFT-Rec ---")
    if _bft_rec_arr is None: 
        print("None")
    else:
        for i in _bft_rec_arr: 
            print(i.nodeVal, end=' ')
    print("\n--- BFT-Iter ---")
    if _bft_iter_arr is None: 
        print("None")
    else:
        for i in _bft_iter_arr: 
            print(i.nodeVal, end=' ')

    print("\n--- Random Directed Acyclic Graph ---")
    topSort_graph = createRandomDAGIter(1000)
    topSort_kahns = TopSort.Kahns(topSort_graph)
    print("--- Topological Sort - Kahns ---")
    if topSort_kahns is None:
        print("None")
    else:
        for i in topSort_kahns: print(i.nodeVal, end=' ')
    topSort_mDFS = TopSort.mDFS(topSort_graph)
    print("\n--- Topological Sort - mDFS ---")
    if topSort_mDFS is None: 
        print("None")
    else:
        for i in topSort_mDFS: 
            print(i.nodeVal, end=' ')

    print("\n--- Random Complete Weighted Graph ---")
    dijkstras_graph = createRandomCompleteWeightedGraph(1000)
    dijkstras_nodes = dijkstras_graph.getAllNodes()
    dijkstras_listOfNodes = list(dijkstras_nodes)
    dijkstras_listOfNodes.sort(key=lambda x: x.nodeVal)
    dijkstras_result = dijkstras(dijkstras_listOfNodes[2])
    print("--- Dijkstras ---")
    if dijkstras_result is None: 
        print("None")
    else:
        for i in dijkstras_result:
            print(i.nodeVal, dijkstras_result[i])

    print("--- Random Grid Graph ---")
    astar_graph = createRandomGridGraph(100)
    astar_nodes = astar_graph.getAllNodes()
    astar_listOfNodes = list(astar_nodes)
    astar_listOfNodes.sort(key=lambda x: x.nodeVal)
    astar_sourceNode = astar_listOfNodes[0]
    astar_dstNode = astar_listOfNodes[9999] 
    astar_result = astar(astar_sourceNode, astar_dstNode)
    if astar_result is None:
        print("None")
    else:
        for i in astar_result:
            print(i.nodeVal, end=' ')

if __name__ == "__main__":
    main()
