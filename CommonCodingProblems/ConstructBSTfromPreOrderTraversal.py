'''
Created on Jan 3, 2020

@author: latikamehra

Given preorder traversal of a binary search tree, construct the BST.

For example, if the given traversal is {10, 5, 1, 7, 40, 50}, then the output should be root of following tree.

     10
   /   \
  5     40
 /  \      \
1    7      50
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
            path = path +self.postOrderTrav(node.right)
            
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
    
    
    def breadthFirstTrav(self, node, parentNode = None):
        allCh = []
        if parentNode == None : allCh = [node]
        allChDesc = []
        
        if node.left != None : 
            allCh.append(node.left.val)
            allChDesc = allChDesc + self.breadthFirstTrav(node.left, node)
        
        if node.right != None :
            allCh.append(node.right.val)
            allChDesc = allChDesc + self.breadthFirstTrav(node.right, node)
            
        allDesc = allCh + allChDesc 
        
        return allDesc
            
        
        


def constructBSTFromPreOrder(preOrdTrav):
    if len(preOrdTrav) == 0 : return None
    
    elif len(preOrdTrav) == 1 : 
        root = TreeNode(preOrdTrav[0])
        return root
    
    else :
        root = TreeNode(preOrdTrav[0])
        flipIndx = None
        
        for i in range(1, len(preOrdTrav)):
            node = preOrdTrav[i]
            
            if node > root.val :
                flipIndx = i 
                break
            
        if flipIndx != None :
            leftNodes = preOrdTrav[1:flipIndx]
            rightNodes = preOrdTrav[flipIndx:]
            
        else :
            leftNodes = preOrdTrav[1:]
            rightNodes = []
            
        
        root.left = constructBSTFromPreOrder(leftNodes)
        root.right = constructBSTFromPreOrder(rightNodes)
        
        return root
    
    
    

traversal = [10,5,1,7,40,50]  

root =  constructBSTFromPreOrder(traversal)

bt = BinaryTree(root)

print (bt.preOrderTrav(root))
        
        
