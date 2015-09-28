def anagram(s1, s2):
    dict={}
    if len(s1) != len(s2):
        return False
    
    for i in range(len(s1)):
        if s1[i] not in dict:
            dict[s1[i]] = 1
        else:
            dict[s1[i]] += 1
            
    for i in range(len(s2)):
        if s2[i] not in dict:
            dict[s2[i]] = -1
            print s2[i]
        else:
            dict[s2[i]] -= 1
            if dict[s2[i]] < 0:
                return False
    return True
    
