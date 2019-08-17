'''
Created on Jul 24, 2019

@author: latikamehra

'''

class PrettyPrint():
    def __init__(self, opWidth=150):
        self.opWidth = opWidth
        self.rcrsnLvl = 0

    def cat(self,rowArray, offset=0): # Print WITHOUT column walls
        formatted_str = ""
        divs = len(rowArray)
        col_width = int((self.opWidth-offset)/divs)
        
        i = 0 # Counter for tuple iteration
        end_point = 0
        for cellStr in rowArray :
            col_stpt = i*col_width + offset
            strlen = len(cellStr)
            
            start_point = col_stpt + int((col_width-strlen)/2)
            
            gap = " "*max((start_point - end_point),1)  # Required number of white spaces to be added is determined by new starting point minus the previous string's end point
            #gap += " "*offset*max((1-i),0) # If the first string is being printed then add the initial offset to the gap as the cursor would be at x=0
            
            formatted_str += gap + cellStr
            
            end_point = start_point + strlen # Compute the new End Point of the string
            
            i += 1
        
        return(formatted_str+"\n")
        
        
    def cat_tabluar(self,rowArray, offset=0): # Print WITH column walls
        formatted_str = ""
        divs = len(rowArray)
        col_width = int((self.opWidth-offset)/divs) - 1
        
        i = 0 # Counter for tuple iteration
        end_point = 0
        for cellStr in rowArray :
            col_stpt = i*col_width + offset
            strlen = len(cellStr)
            
            start_point = col_stpt + int((col_width-strlen)/2)
            
            gap1 = " "*max((col_stpt - end_point),1) 
            
            gap2 = " "*max((start_point - col_stpt),1) 
            
            formatted_str += gap1 + "|" + gap2 + cellStr
            
            end_point = start_point + strlen # Compute the new End Point of the string
            
            i += 1
        
        formatted_str += " "*(self.opWidth - end_point - divs - 1) + "|"
        return(formatted_str+"\n")
    
    
    def collectionPrnt(self, cllctn, tabCnt=0, initialOffset=0):
        self.rcrsnLvl += 1
        #print ("Recursion Level = "+str(self.rcrsnLvl))
        
        if type(cllctn) in (set, tuple) : 
            brack = ("(", ")")
            sep = " , "
        elif type(cllctn) == list : 
            brack = ("[", "]")
            sep = " , "
        elif type(cllctn) == dict : 
            brack = (" "*initialOffset+"{\n"+ "\t"*tabCnt, "\n"+"\t"*tabCnt+"}")
            sep = ",\n" + "\t"*tabCnt
        else : 
            brack = ("", "")
            sep = " , "
        
        formatted_str = []
        
        if type(cllctn) == dict: 
            for key, val in cllctn.items() :
                keyStr = str(key)+ " => "
                reqdTabs = tabCnt + len(keyStr)//8 + 1
                initOffst = (8 - len(keyStr)%8)
                keyStr += self.collectionPrnt(val, tabCnt=reqdTabs, initialOffset=initOffst)
                formatted_str.append(keyStr)
         
        elif type(cllctn) in (list, set, tuple) :
            for c in cllctn:
                formatted_str.append(self.collectionPrnt(c))
        else: 
            return(str(cllctn))

        
        finStr = brack[0] +  sep.join(formatted_str) + brack[1] 
        
        #print (finStr)
        return (finStr+"\n")
            

        