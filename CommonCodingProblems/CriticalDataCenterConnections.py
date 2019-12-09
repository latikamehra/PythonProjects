'''
Created on Dec 5, 2019

@author: latikamehra
Given a data center with n servers from 1 to n. To make the data center running, all servers must be connected, that means there exists at least one path between any pair of servers. Now we know there could be some cirtical connections broken which brings down the whole data center. You need to write a program to find out all these broken cirtical connections. A server connection is a cirtical connection which when removed will make the whole data center disconnected.
Write a method to output all critical connections.

Input:
serversNum, the number of servers in the data center.
connectionsNum, the number of connections between the servers.
connections, a list of pairs reperesting the connections between two severs.

Output:
Return a list of integer pairs representing the cirtical connections. Output an empty array if there are no cirtical connections.
Example :
Input:
serversNum = 4
connectionsNum = 4
connections = [[1, 2], [1, 3], [3, 2], [3, 4]]

Output:
[[3,4]]
Explanation:
There are one cirtical connections:
1. Between server 3 and 4
If the connection [3, 4] breaks, then the network will be disconnected since servers 3 and 4 cannot communicate with the rest of the network.
Remaining three connections are not cirtical.
'''

def findAllNodes(servNum):
    nodeArr = []
    for i in range(1,servNum+1):
        nodeArr.append(i)
        
    return nodeArr

def constrConnDict(nodes, conns):
    graph = {}
    
    for i in range(0,len(nodes)) :
        node = nodes[i]
        graph[node] = []
        for conn in conns :
            if conn[0] == node : graph[node].append(conn[1])
            if conn[1] == node : graph[node].append(conn[0])
            
    return (graph)
        

def findPossiblePaths(graph, start, end, paths = []): 
    pathSet = []   
    paths = paths + [start]
    
    if start == end : 
        return [paths]
    if start not in graph.keys() :
        return None
    for node in graph[start] :
        if node not in paths :
            newpaths = findPossiblePaths(graph, node, end, paths)
            if newpaths : 
                for newpath in newpaths : 
                    pathSet.append(newpath)
    
    return pathSet
        
        
def constrUniqueList(arrList):
    unqList = []
    for arr in arrList :
        if arr not in unqList : unqList.append(arr)
        
    return unqList
        
    

def findCriticalConn(servNum, connNum, conns):
    criticalConns = []
    criticalPaths = []
    nodes = findAllNodes(servNum)
    ln = len(nodes)
    graphDict = constrConnDict(nodes, conns)
    #print(graphDict)
    
    for i in range(0, ln) :
        for j in range(i+1, ln) :
            n1 = nodes[i]
            n2 = nodes[j]
            
            possPaths = findPossiblePaths(graphDict,n1,n2)
            
            #print (n1, n2)
            #print (possPaths)
            
            pathCnts = len(possPaths)
            
            if pathCnts == 1 :
                criticalPaths.append(possPaths[0])
                
                
    #print (criticalPaths)
    
    for critP in criticalPaths :
        for i in range(0,len(critP)-1) :
            criticalConns.append([critP[i], critP[i+1]])
            
            
    criticalConnections = constrUniqueList(criticalConns)
    print (criticalConnections)
                
            
            
        
    
    
    
    
 
serversNum = 5
connectionsNum = 4
connections = [[1,2], [2,3], [3,4], [4,5], [3,5]]  

findCriticalConn(serversNum, connectionsNum, connections)

    
    
