def shortestDistance(words,word1, word2):
    distance = float("infinity")
    index1 = 0 
    index2 = 0
    for index in range(len(words)):
        if words[index] == word1:
            index1 = index
        if words[index] == word2:
            index2 = index
        
    distance = min(distance, abs(index2-index1))
    return distance

        
    
print shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice")
print shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "makes")

