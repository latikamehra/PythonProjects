'''
Created on Dec 30, 2019

@author: latikamehra


Given a binary tree and a list of nodes say [n1, n2, .. nk], write a program to find the least common ancestor.

'''
''' Represent Binary Tree in Python :

      tree
      ----
       1    <-- root
     /   \
    2     3  
   /   
  4

class Node :
    def __init__(self,key) :
        self.left = None
        self.right = None
        self.val = key
        

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

'''

class TreeNode :
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
        self.level = None


class BinaryTree :
    
    def __init__(self,dct):
        self.dct = dct
        self.binTree = []
        self.root = None
        
        self.findAllNodes()
        self.buildTree()
        self.findRoot()
        #self.printTree(self.root)
        self.findLevels(self.root, 0)
        
        #self.printTreeLevs()
        
        
    def printTree(self, rootNode):
        
        if rootNode.left != None : 
            leftChild = str(rootNode.left.val)
        else : 
            leftChild = ""
        if rootNode.right != None : 
            rightChild = str(rootNode.right.val)
        else : 
            rightChild = ""
        
        msg = str(rootNode.val) + " => [ " + leftChild + " , " + rightChild + " ]"
        print (msg)
        
        if rootNode.left != None : self.printTree(rootNode.left)
        if rootNode.right != None : self.printTree(rootNode.right)         
        
        
    def printTreeLevs(self):
        for nd in self.binTree :
            print (nd.val, nd.level)
    
    def findAllNodes(self):
        self.allNodes = []
        for key, val in self.dct.items() :
            nds = (key, val[0], val[1])
            for nd in nds :
                if nd not in self.allNodes and nd != None : self.allNodes.append(nd)
                    
            
    def buildTree(self):
        #print (self.allNodes)
        treeDct = {}
        for nd in self.allNodes :
            treeDct[nd] = TreeNode(nd)
            
        
        for nd in self.allNodes :
            if nd in self.dct.keys() :
                if self.dct[nd][0] != None : 
                    treeDct[nd].left = treeDct[self.dct[nd][0]]
                if self.dct[nd][1] != None : 
                    treeDct[nd].right = treeDct[self.dct[nd][1]]
            
            #print (thisNode.val, thisNode.left, thisNode.right)
            self.binTree.append(treeDct[nd])
            
            
    def findRoot(self):
        allNodes = []
        notRoot = []
        for btNode in self.binTree :
            allNodes.append(btNode.val)
            if btNode.left != None : notRoot.append(btNode.left.val)
            if btNode.right != None : notRoot.append(btNode.right.val)
            
            
        nodeSet = set(allNodes)
        notRootSet = set(notRoot)
        
        rootNode = list(nodeSet.difference(notRootSet))[0]
        
        for nd in self.binTree :
            if nd.val == rootNode : self.root = nd
            
            
    def findLevels(self, rootNode, lev):
        #print ("Node = "+str(rootNode.val))
        #print ("Level = "+str(lev))
        #print ("Left Child = "+str(rootNode.left.val))
        rootNode.level = lev
        
        if rootNode.left != None : self.findLevels(rootNode.left, lev+1) 
        if rootNode.right != None : self.findLevels(rootNode.right, lev+1) 
    
    
    def findParent(self, node):
        for btNode in self.binTree :
            if btNode.left != None :
                if btNode.left.val == node : 
                    return btNode
                
            if btNode.right != None :
                if btNode.right.val == node : 
                    return btNode
                
                
        return None
                
                
    def findAllAncestors(self, node, ancestorList = []):
        parent = self.findParent(node)
        newAncList = ancestorList.copy()
        
        if parent != None :
            newAncList.append(parent)
            
            newAncList = newAncList + self.findAllAncestors(parent.val, newAncList)
            
            return newAncList
        
        else : return []
        
        
        
    def commonAncestors(self, ancestorLists):
        commonAncestors = []

        for ancestor in ancestorLists[0] :
            flag = True
            for i in range(1, len(ancestorLists)) :
                if ancestor not in ancestorLists[i] : flag = False
                
            
            if flag == True : commonAncestors.append(ancestor)
            
            
        return commonAncestors
    
    
    
    def lca(self, commonAncestors):
        maxLev = 0
        lca = None
        
        for ca in commonAncestors :
            if ca.level >= maxLev :
                maxLev = ca.level
                lca = ca.val
 
                
        return lca
            
        

def findLCA(binTreeObj, nodeList):
    allAncLists = []
    for nd in nodeList :
        ancList = binTreeObj.findAllAncestors(nd)
        allAncLists.append(ancList)
        
    commAnc = binTreeObj.commonAncestors(allAncLists)
    
    lcaVal = binTreeObj.lca(commAnc)
    
    return lcaVal
        
        
    
    

    
inputTreeDict = {5 : (10, None),
                 6 : (None, 11),
                 7 : (12,13),
                 1 : (2,3),
                 2 : (4,5),
                 3 : (6,7),
                 4 : (8,9),
                 13 : (14, None)}


nodeList = [13,14,6]

bt = BinaryTree(inputTreeDict)

lca = findLCA(bt, nodeList)
print (lca)    
    
   
