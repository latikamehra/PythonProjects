'''
Created on Jan 1, 2020

@author: latikamehra

Subtree with Maximum Average

Given a M-ary tree, find the subtree with maximum average. Return the root of the subtree.
A subtree of a tree is any node of that tree plus all its descendants. The average value of a subtree is the sum of its values, divided by the number of nodes.
'''

class TreeNode :
    def __init__(self,val):
        self.val = val
        self.children = []
        self.avg = None
        
        
def createInputTree():
    root = TreeNode(1)
    root.children = [TreeNode(-5), TreeNode(13), TreeNode(4)]
    
    root.children[0].children = [TreeNode(1), TreeNode(2)]
    root.children[1].children = [TreeNode(4), TreeNode(-2)]
    
    return root

            
 
def avgSubTree(node):
    if node.children == [] :
        node.avg = node.val
        return (node.val,1)
    else :
        denom = 1
        numer = node.val
        for ch in node.children :
            chAvg , chChildCount = avgSubTree(ch)
            numer += chAvg*chChildCount
            denom += chChildCount
            
        avg = float(numer)/float(denom)   
        
        node.avg = avg    
        return (avg, denom)


def traverseTree(node):
    nodes = [node]
    
    if node.children == []:
        return nodes
    else :
        for ch in node.children :
            nodes += traverseTree(ch)
            
    return nodes
            
 
def maxSubTreeAvg(root):
    avgSubTree(root)
    nodes = traverseTree(root)
    maxAvg = nodes[0].avg
    bestNode = nodes[0].val
    for node in nodes :
        if node.avg > maxAvg :
            maxAvg = node.avg
            bestNode = node.val
            
    print ("Value of the node with maximum sub-tree average : "+str(bestNode))
    print ("Maximum average = "+str(maxAvg))
        
        

    
    
root = createInputTree()  

maxSubTreeAvg(root)
            
            
