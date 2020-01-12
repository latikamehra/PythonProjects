'''
Created on Jan 3, 2020

@author: latikamehra
'''

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        
def breadthFirstTrav(node, parentNode = None):
        
        if parentNode == None : allCh = [node.val]
        else: allCh = []
            
        allChDesc = []
        
        if node.left != None : 
            allCh.append(node.left.val)
            allChDesc = allChDesc + breadthFirstTrav(node.left, node)
        
        if node.right != None :
            allCh.append(node.right.val)
            allChDesc = allChDesc + breadthFirstTrav(node.right, node)
        
        allDesc = allCh + allChDesc 

        return allDesc  
    
           
def isAncestor(possAncestor, node): 
    if node == possAncestor : return True 
    
    else :
        if possAncestor.left != None :
            if isAncestor(possAncestor.left, node) == True : return True
            
        if possAncestor.right != None :
            if isAncestor(possAncestor.right, node) == True : return True  
            
    
    return False
            
            
            
            
    

def lca(root, nodes):
    isAncestor(root, root)          

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

'''
for n in nodeStack :
    msg = str(n.val) + "-->"
    if n.left : msg += str(n.left.val) + " , "
    else : msg += "None , "
    if n.right : msg += str(n.right.val) + " , "
    else : msg += "None"
    print (msg)
'''

print (breadthFirstTrav(root))
