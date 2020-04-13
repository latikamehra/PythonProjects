class Solution:
        
    def isMatch(self, s, p) :
        if len(s) == 0 :
            if len(p) == 0 :
                return True
            elif len(p) == 1 :
                if p[0] == "*" :
                    return True
                else :
                    return False
            else :
                if p[0] == "*" :
                    return self.isMatch(s, p[1:])
                elif p[1] == "*" :
                    return self.isMatch(s, p[2:])
                else :
                    return False
            
        else :
            if len(p) == 0 :
                return False
            elif len(p) == 1 :
                char = p[0]
                if char == ".":
                    if len(s) == 1 :
                        return True
                    else :
                        return False
                elif char == "*" :
                    return True
                else :
                    if len(s) == 1 and s[0] == char:
                        return True
                    else :
                        return False 
            else :
                char1 = p[0]
                char2 = p[1]
                
                if char1 == "." :
                    if char2 == "*" :
                        if len(p) == 2 :
                            return True
                        else :
                            char = p[2]
                            if char == "." :
                                return self.isMatch(s, p[2:])
                            elif char in s :
                                ind = s.index(char)
                                return self.isMatch(s[ind:], p[2:])
                            else :
                                return False
                        return self.isMatch(s, p[2:])
                    else :
                        return self.isMatch(s[1:], p[1:])
                    
                elif char2 == "*" :
                    ind = 0
                    for i in range(0, len(s)) :
                        if char1 == s[i] :
                            ind += 1
                        else:
                            break
                                
                    if ind >= len(s) : 
                        return True   
                    else :
                        return self.isMatch(s[ind:], p[2:])
                
                else :
                    if s[0] == char1 :
                        return self.isMatch(s[1:], p[1:])
                    else:
                        return False
                                    
                        
                    
                    
                    
        
        