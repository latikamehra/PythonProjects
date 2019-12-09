'''
Created on Dec 6, 2019

@author: latikamehra
There's an undirected connected graph with n nodes labeled 1..n. But some of the edges has been broken disconnecting the graph. Find the minimum cost to repair the edges so that all the nodes are once again accessible from each other.

Input:
n, an int representing the total number of nodes.
edges, a list of integer pair representing the nodes connected by an edge.
edgesToRepair, a list where each element is a triplet representing the pair of nodes between which an edge is currently broken and the cost of repearing that edge, respectively (e.g. [1, 2, 12] means to repear an edge between nodes 1 and 2, the cost would be 12).

Example 1:
Input:
n = 5, edges = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], edgesToRepair = [[1, 2, 12], [3, 4, 30], [1, 5, 8]]
Output: 20
Explanation:
There are 3 connected components due to broken edges: [1], [2, 3] and [4, 5].
We can connect these components into a single component by repearing the edges between nodes 1 and 2, and nodes 1 and 5 at a minimum cost 12 + 8 = 20.

Example 2:
Input:
n = 6, edges = [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]], edgesToRepair = [[1, 6, 410], [2, 4, 800]]
Output: 410

Example 3:
Input:
n = 6, edges = [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]], edgesToRepair = [[1, 5, 110], [2, 4, 84], [3, 4, 79]]
Output: 79
'''
from gettext import lngettext

def constrCombFromBin(arr, binStr):
    newArr = []
    for i in range(0,len(binStr)) :
        if binStr[i] == '1' : newArr.append(arr[i])
    return newArr
        
    

def constrAllPossibleSets(arr):
    arrSet = []
    ln = len(arr)
    combSz = 2**ln 
    for i in range(0,combSz) :
        binEq = str(bin(i))
        binEq = binEq.replace('0b',"")
        zeroPadding = "0"*(ln - len(binEq))
        binEq = zeroPadding + binEq
        
        #print (binEq)
        comb = constrCombFromBin(arr, binEq)
        arrSet.append(comb)
        
    #print(arrSet)    
    return arrSet
        
        
    

def constrNodeList(numNodes):
    nodes = [None]*numNodes
    for i in range(1, numNodes+1):
        nodes[i-1] = i 
        
    return nodes
    
def constrBidirGraph(nodes, edges):
    graphDict = {}
    for node in nodes :
        graphDict[node] = []
        for edge in edges :
            if edge[0] == node : graphDict[node].append(edge[1])
            if edge[1] == node : graphDict[node].append(edge[0])
            
            
    return graphDict
            
      
def areNodesConnected(graph, startNode, endNode, path=[]):
    path = path + [startNode]
    if startNode == endNode :
        return True

    if startNode in graph.keys() and endNode in graph.keys() :
        for node in graph[startNode] :
            if node not in path :
                newPath = areNodesConnected(graph, node, endNode, path)
                if newPath == True : return True
        
    return False


def isGraphConnected(graph, nodes):
    for n in range(1,len(nodes)) :
        if areNodesConnected(graph, nodes[0], nodes[n]) == False : 
            return False
        
    return True
 
def constrDamagedEdges(edgesToRepair):
    damagedEdges = []
    for er in edgesToRepair :
        damagedEdges.append(er[0:2])

    return damagedEdges
     
        
def constrDamagedGraph(nodes, allEdges, damagedEdges):
    goodEdges = []
    for edge in allEdges : 
        if edge not in damagedEdges : goodEdges.append(edge)
        
    damagedGraph = constrBidirGraph(nodes, goodEdges)
        
    return damagedGraph

def findRepairCostOfSet(repSet, toRepairMap):
    cost = 0
    for rs in repSet :
        for rm in toRepairMap :
            if rs[0] == rm[0] and rs[1] == rm[1] : cost += rm[2]
            
    return cost

        
def computeMaxCost(toRepair): 
    mc = 0
    for tr in toRepair:
        mc += tr[2]
        
    return mc
            
    
def minCostOfRepair(nodeNum, allEdges, toRepair):   
    nodeList = constrNodeList(nodeNum)
    fullGraph = constrBidirGraph(nodeList, edges)
    allDamagedEdges = constrDamagedEdges(toRepair)
    damagedGraph = constrDamagedGraph(nodeList, allEdges, allDamagedEdges)
    
    #print(allDamagedEdges)
    #print(damagedGraph)
    if isGraphConnected(damagedGraph, nodeList) : return (0,0)
    
    possRepairSets =  constrAllPossibleSets(allDamagedEdges)
    maxCost = computeMaxCost(toRepair)
    bestRepairSet = []
    
    #print(possRepairSets)
    
    for repSet in possRepairSets :
        stillDamagedEdges = []
        for ade in allDamagedEdges :
            if ade not in repSet : stillDamagedEdges.append(ade)
            
        
        #print(stillDamagedEdges)
        repairedGraph = constrDamagedGraph(nodeList,allEdges,stillDamagedEdges)
        #print(repairedGraph)
        
        if isGraphConnected(repairedGraph, nodeList) == True: # Graph successfully repaired
            cost = findRepairCostOfSet(repSet, toRepair)
            #print("Graph Repaired with ")
            #print (repSet)
            #print(cost)
            if cost < maxCost : 
                maxCost = cost
                bestRepairSet = repSet

    return (bestRepairSet, maxCost)
                
            
        
        
    
      
        
nodeNum = 6
edges = [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]]
edgesToRepair = [[1, 6, 410], [2, 4, 800]]

bestRepairSet, minCost = minCostOfRepair(nodeNum, edges, edgesToRepair)

print ("Best Repair Set :")
print(bestRepairSet)
print ("Minimum Cost :")
print(minCost)