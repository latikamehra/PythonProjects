'''
Created on Jan 3, 2020

@author: latikamehra

Cut BST

Given a BST, and an integer k, cut the BST vertically into two substrees A and B, where all nodes in A <= k and all nodes in B > k.

Constrain: for any node A and it’s parent B in the original BST. If after the cut they are both in the same subtree. B should still be the parent of A.

 

example:

Input:

           50

        /      \

      20       60

     /   \    /  \

   10   30   55   70

k = 50

 

output:

 

      20         

     /   \        

   10   30   

 

and 

      60

     /   \         

   55   70
'''


