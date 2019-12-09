'''
Created on Dec 6, 2019

@author: latikamehra

Given a map Map<String, List<String>> userMap, where the key is a username and the value is a list of user's songs. Also given a map Map<String, List<String>> genreMap, where the key is a genre and the value is a list of songs belonging to this genre. The task is to return a map Map<String, List<String>>, where the key is a username and the value is a list of the user's favorite genres. 
Favorite genre is a genre with the most song.
'''

def reverseGenreMap(genreMap):
    songGenreMap = {}
    for genre, songs in genreMap.items() :
        for song in songs :
            songGenreMap[song] = genre 
            
    return songGenreMap
        
    

def favGenres(userMap, genreMap):
    songGenreMap = reverseGenreMap(genreMap)
    
    userTopGenre = {}
    
    for user, songs in userMap.items() :
        userTopGenre[user] = []
        genreCount = {}
        for song in songs :
            genre = songGenreMap[song]
            genreCount.setdefault(genre, 0)
            genreCount[genre] = genreCount[genre] + 1
        
        maxCnt = 0    
        for genre, cnt in genreCount.items() :
            if cnt > maxCnt : maxCnt = cnt
            
        for genre, cnt in genreCount.items() :
            if cnt == maxCnt :
                userTopGenre[user].append(genre)
                
                
                
                
    return userTopGenre





userMap = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}

genreMap = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

print (favGenres(userMap, genreMap))