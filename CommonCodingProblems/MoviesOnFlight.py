'''
Created on Dec 29, 2019

@author: latikamehra

You are on a flight and wanna watch two movies during this flight.
You are given int[] movie_duration which includes all the movie durations.
You are also given the duration of the flight which is d in minutes.
Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).
Find the pair of movies with the longest total duration. If multiple found, return the pair with the longest movie.

e.g.
Input
movie_duration: [90, 85, 75, 60, 120, 150, 125]
d: 250

Output from aonecode.com
[90, 125]
90min + 125min = 215 is the maximum number within 220 (250min - 30min)
'''



def longest2Movies(totalTime, movArr):
    
    sortedArr = movArr.copy()
    sortedArr.sort(reverse=True)
    
    bestTime = 0
    bestSet = None
    
    for i in range(0,len(sortedArr)) :
        for j in range(i+1,len(sortedArr)) :
        
            timeTaken = sortedArr[i] + sortedArr[j]
            if totalTime >= timeTaken :
                if timeTaken > bestTime :
                    bestTime = timeTaken
                    bestSet = (sortedArr[i] , sortedArr[j])
                    
                    
                    
                    
    return bestSet


movArr = [90, 85, 75, 60, 120, 150, 125, 110,105]
d = 250
print (longest2Movies(d-30, movArr))
                
            
        
        

