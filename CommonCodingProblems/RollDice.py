'''
Created on Dec 10, 2019

@author: latikamehra
A six-sided dice is a small cube with a different number of pips. Each face(side) ranging from 1 to 6.
On any two opposite side of the cube, the number of pips adds up to 7; that is, there are three pairs of opposite sides: 1 and 6, 2 and 5, and 3 and 4.
There are N dice lying on a table, each showing the pips on its top face. In one move, you can take one dice and rotate it to an adjacent face.
For example, you can rotate a dice that shows 1 to show 2, 3, 4 or 5. However, it cannot show 6 in a single move, because the faces with one pip and six pips visible are opposite sides rather than adjacent.
You want to show the same number of pips on the top face of all N dice. Given that each of the dice can be moved multiple times, count the minimum number of moves needed to get equal faces.

Write a function:
that, given an array A consisting of N integers describing the number of pips (from 1 to 6) shown on each dice’s top face, returns the minimum number of moves necessary for each dice show the same number of pips.

For example, given:
• A = [1, 2, 3], the function should return 2, as you can pick the first two dice and rotate each of them in one move so that they all show three pips on the top face. Notice that you can also pick any other pair of dice in this case.
• A = [1, 1, 6], the function should also return 2. The only optimal answer is to rotate the last dice so that it shows one pip. It is necessary to use two rotations to achieve this.
• A = [1, 6, 2, 3], the function should return 3. For instance, you can make all dice show 2: just rotate each dice which is not showing 2 (and notice that for each dice you can do this in one move).
'''


def rotateDice(arr):
    diceArr = [1,2,3,4,5,6]
    
    minRots = maxRots = 2*len(arr)
    
    for finFace in diceArr :
        reqdRot = 0
        for dice in arr :
            if finFace+dice == 7 : reqdRot += 2
            elif finFace != dice : reqdRot += 1
        
        #print ("Face = "+str(finFace) +" Rotations = "+ str(reqdRot))
            
        if reqdRot <= minRots : 
            minRots = reqdRot
            finalFace = finFace
            
            
    print ("Minimum Rotations Required = " +str(minRots) )
    print ("With final face = "+str(finalFace))
    
    
diceArr = [1,5,4,3,3,4,4,5,6,6,6,1,1,1,2,3,4,5,6,4,4]

rotateDice(diceArr)
    
            
        
