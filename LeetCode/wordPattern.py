def wordPattern(pattern, string):
    wordList = string.split()
    if len(wordList) != len(pattern):
        return False
    

print wordPattern("abab", "dog cat dog cat") #True
print wordPattern("aaaa", "dog dog dog dog") #True
print wordPattern("abab", "cat cat cat cat") #False
