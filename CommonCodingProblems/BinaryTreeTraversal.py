'''
Created on Jan 3, 2020

@author: latikamehra
'''

class TreeNode:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None
        
        
class BinaryTree :
    def __init__(self,root):
        self.root = root
        
    
    def preOrderTrav(self, node):
        path = [node.val]
        
        if node.left != None : 
            path = path + self.preOrderTrav(node.left)
        if node.right != None :
            path = path +self.preOrderTrav(node.right)

        return path
            
        
    def postOrderTrav(self, node):
        path = []
        
        if node.left != None : 
            path = path + self.postOrderTrav(node.left)
        if node.right != None :
            path = path + self.postOrderTrav(node.right)
            
        path.append(node.val)
        return path
    
        
    def inOrderTrav(self, node):
        path = []
        
        if node.left != None : 
            path = path + self.inOrderTrav(node.left)
            
        path.append(node.val)
        
        if node.right != None :
            path = path +self.inOrderTrav(node.right)

        return path
    
    
    def breadthFirstTravDct(self, node, level=0, pathMap={}):
        if node == None : return pathMap
        
        pathMap.setdefault(level, [])
        pathMap[level].append(node.val)
        
        pathMap = self.breadthFirstTravDct(node.left, level+1, pathMap)
        pathMap = self.breadthFirstTravDct(node.right, level+1, pathMap)
        
        return pathMap
    
    
    def breadthFirstTrav(self, node):
        pathMap = self.breadthFirstTravDct(node)
        path = []
        for key in sorted(pathMap.keys()):
            path = path + pathMap[key]
            
        return path
            
        
        
        

    
    
    
    
def createInputTree(nodeNum):
    nodeStack = []
    
    for i in range(0, nodeNum) :
        nodeStack.append(TreeNode(i+1))
        
    root = nodeStack[0]
    ptr = 1
    for i in range(0, nodeNum) :
        currNode = nodeStack[i]
        if ptr < nodeNum :
            currNode.left = nodeStack[ptr]
            ptr += 1
        if ptr < nodeNum :
            currNode.right = nodeStack[ptr]
            ptr += 1
    
    return root, nodeStack


root, nodeStack = createInputTree(15)

bt = BinaryTree(root)
nlr = bt.preOrderTrav(root)
lnr = bt.inOrderTrav(root)
lrn = bt.postOrderTrav(root)
bfs = bt.breadthFirstTrav(root)



paths = [nlr, lnr, lrn, bfs]
for path in paths :
    print (path)
