'''
Created on Dec 9, 2019

@author: latikamehra

Given an undirected graph with n nodes labeled 1..n. Some of the nodes are already connected. The i-th edge connects nodes edges[i][0] and edges[i][1] together. Your task is to augment this set of edges with additional edges to connect all the nodes. Find the minimum cost to add new edges between the nodes such that all the nodes are accessible from each other.

Input:
n = 6, edges = [[1, 4], [4, 5], [2, 3]], newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
Output: 7
'''

def nCk_combinationSelector(availArr, numOfElems, existingArr=[]):
    arrSz = len(availArr)
    resArrArr = []
    
    
    if numOfElems > arrSz :
        return None
    
    elif numOfElems == arrSz :
        newArr = existingArr + availArr
        resArrArr.append(newArr)
    
    elif numOfElems == 1 :
        for e in availArr :
            newArr = existingArr + [e]
            resArrArr.append(newArr)
    
    elif numOfElems == 0 :
        resArrArr = [[]]
    
    elif numOfElems < arrSz :
        newAvailArr = availArr.copy()
        for e in availArr :
            newExistingArr = existingArr + [e] 
            newAvailArr.remove(e)
            newNumOfElems = numOfElems - 1
            
            thisresArrArr = nCk_combinationSelector(newAvailArr, newNumOfElems, newExistingArr)
            
            if thisresArrArr != None :
                resArrArr += thisresArrArr
    
    
    return resArrArr

def allPossibleCombinations(arr):
    resArrArr = []
    
    for i in range(0,len(arr)+1) :
        iCombs = nCk_combinationSelector(arr, i)
        resArrArr += iCombs
        
    return resArrArr


    
def areNodesConnected(graph, start, end, path=[]): 
    newPath = path + [start]
    
    if start == end :
        return True
    
    if start in graph.keys() and end in graph.keys() :
        for nxtNode in graph[start] :
            if nxtNode not in path :
                if areNodesConnected(graph, nxtNode, end, newPath) == True : return True
            
   
    return False
       
    

def isGraphConnected(graph, nodes):
    for i in range(1, len(nodes)) :
        if areNodesConnected(graph, nodes[0], nodes[i]) != True : return False
        
    return True
        
 
 
def constrNewEdgeDict(newEdges):
    edgeDict = {}
    edgeCostDict = {}
    
    index = 1
    for e in newEdges :
        edgeDict[index] = e[0:2]
        edgeCostDict[index] = e[2]
        index += 1
        
        
    return (edgeDict, edgeCostDict)


def constrNodeList(numNodes): 
    nodeList = []
    for i in range(1, numNodes+1) :
        nodeList.append(i)
        
    return nodeList


def constrGraph(edges, nodes):
    graph = {}
    
    for node in nodes :
        graph[node] = []
        for e in edges :
            if e[0] == node : graph[node].append(e[1])
            if e[1] == node : graph[node].append(e[0])
            
    return graph

 
 
def minCostToConnectGraph(nodeNum, edges, newEdges):
    nodeList = constrNodeList(nodeNum)
    edgeDict, edgeCostDict =  constrNewEdgeDict(newEdges)   
    
    newEdgeList = list(edgeDict.keys())
    #print (newEdgeList)
    
    maxCost = 0
    edgesToBeAdded = None
    for c in edgeCostDict.values() : 
        maxCost += c
    
    allPossCombsOfNewEdges = allPossibleCombinations(newEdgeList)
    
    for comb in allPossCombsOfNewEdges :
        #print (comb)
        cost = 0
        newEdgeList = []
        for edgeKey in comb :
            newEdgeList.append(edgeDict[edgeKey])
            cost += edgeCostDict[edgeKey]
    
        edgeSet = edges + newEdgeList
       
        graph = constrGraph(edgeSet, nodeList)
       
        if isGraphConnected(graph, nodeList) == True :
            if cost < maxCost : 
                maxCost = cost 
                edgesToBeAdded = newEdgeList 
               
               
       
    if edgesToBeAdded != None :        
        print ("Max Cost = " + str(maxCost))
        print ("Edges to be added ")
        print (edgesToBeAdded)
    else : 
        print ("The new edges are not sufficient to connect the graph")

         
 
 
 
n = 6
edges = [[1, 4], [4, 5], [2, 3]]
newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]         

minCostToConnectGraph(n, edges, newEdges)
    
    
    
    
    
            
        




