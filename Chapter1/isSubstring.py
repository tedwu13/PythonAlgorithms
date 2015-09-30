def isSubString(s1, s2):
    if s1.find(s2) == -1:
        return False
    else: 
        return True

def checkSubString(s1,s2):
    doubleString = s1+s1
    print doubleString
    return isSubString(doubleString, s2)
    
print checkSubString("waterbottle","erbottlewat")
            
