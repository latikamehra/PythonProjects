'''
Created on Jan 3, 2020

@author: latikamehra
Given a Binary Tree, convert it to a Binary Search Tree. The conversion must be done in such a way that keeps the original structure of Binary Tree.

Input:
          10
         /  \
        2    7
       / \
      8   4
Output:
          8
         /  \
        4    10
       / \
      2   7
'''


class TreeNode:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None
        
        
def descendantCount(node):
    cntr = 0
    
    if node.left != None:
        cntr += 1
        cntr += descendantCount(node.left)
    if node.right != None :
        cntr += 1
        cntr += descendantCount(node.right)
        
    return cntr
    
              
         
        
def preOrderTrav(node):
    path = [node.val]
    
    if node.left != None : 
        path = path + preOrderTrav(node.left)
    if node.right != None :
        path = path +preOrderTrav(node.right)

    return path
        
def breadthFirstTravDct(node, level=0, pathMap={}):
    if node == None : return pathMap
    
    pathMap.setdefault(level, [])
    pathMap[level].append(node.val)
    
    pathMap = breadthFirstTravDct(node.left, level+1, pathMap)
    pathMap = breadthFirstTravDct(node.right, level+1, pathMap)
    
    return pathMap


def breadthFirstTrav(node):
    pathMap = breadthFirstTravDct(node)
    path = []
    for key in sorted(pathMap.keys()):
        path = path + pathMap[key]
        
    return path
    
    

def constructBST(node, valArr = None): 
    if valArr == None : valueArr = preOrderTrav(node)
    else : valueArr = valArr.copy()
    
    valueArr.sort()
    
    if node.left != None :
        leftNodesCount = descendantCount(node.left) + 1
    else:
        leftNodesCount = 0
    
    rootVal = valueArr[leftNodesCount]   
    newRoot = TreeNode(rootVal)
    
    leftValArr = valueArr[0:leftNodesCount]
    rightValArr = valueArr[leftNodesCount+1 :]
    
    if node.left != None :
        newRoot.left = constructBST(node.left, leftValArr)
        
    if node.right != None :
        newRoot.right = constructBST(node.right, rightValArr)
    
    return newRoot
    
    
        
        
        
def createInputTree():
    root = TreeNode(10)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(4)
    
    return root 


root = createInputTree()

bstRoot = constructBST(root)

print (preOrderTrav(bstRoot))

print (breadthFirstTrav(bstRoot))

