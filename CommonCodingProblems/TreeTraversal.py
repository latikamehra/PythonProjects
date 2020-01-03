'''
Created on Jan 2, 2020

@author: latikamehrafa

Traverse a tree in 2 different ways  :
1. Breadth First
2. Depth First
'''

class TreeNode :
    def __init__(self, key):
        self.val = key
        self.children = []
        
        
class Tree :
    def __init__(self,root):
        self.root = root 
        
    
    def breadthFirst(self, node, parent = None):
        if parent == None :
            chNodes = [node.val]
        else:
            chNodes = []
            
        chNodeDesc = []
            
        if node.children == [] :
            return []
        else:
            for ch in node.children :
                chNodes.append(ch.val)
                chNodeDesc = chNodeDesc + self.breadthFirst(ch, node)
                
            allDesc = chNodes + chNodeDesc
        
            return allDesc

        
        
    def depthFirstPreOrder(self,node):
        newPath = [node.val]

        if node.children != [] :
            for ch in node.children :
                newPath = newPath + self.depthFirstPreOrder(ch)
                
        return newPath
    
    
    def depthFirstPostOrder(self,node):
        newPath = []

        if node.children != [] :
            for ch in node.children :
                newPath = newPath + self.depthFirstPostOrder(ch)
        
        newPath.append(node.val)      
          
        return newPath
            
        
        
        
    
    
    


def createInputTree():
    root = TreeNode(1)
    root.children = [TreeNode(2), TreeNode(3), TreeNode(4)]
    
    root.children[0].children = [TreeNode(5), TreeNode(6)]
    root.children[1].children = [TreeNode(7), TreeNode(8)]
    root.children[2].children = [TreeNode(9)]
    
    return root


ipTreeRoot = createInputTree()

tr = Tree(ipTreeRoot)
nodesBFS = tr.breadthFirst(ipTreeRoot)
nodesDFS_PreOrder = tr.depthFirstPreOrder(ipTreeRoot)
nodesDFS_PostOrder = tr.depthFirstPostOrder(ipTreeRoot)

print (nodesBFS)
print (nodesDFS_PreOrder)
print (nodesDFS_PostOrder)