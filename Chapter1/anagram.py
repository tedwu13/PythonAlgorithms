def anagram(s1, s2):
    dict={}
    #check the lengths 
    if len(s1) != len(s2):
        return False
    
    for char in s1:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1

    for char in s2:
        if char in dict:
            if dict[char] == 0: 
                return False
            dict[char] -= 1
        else:
            return False
    return True
    


#anagram 

print anagram("abba", "baba")
