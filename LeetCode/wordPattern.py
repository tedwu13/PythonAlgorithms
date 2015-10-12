def wordPattern(pattern, str):
    words = str.split()  # Space: O(n)
    if len(pattern) != len(words):
        return False

    words, pattern = {}, {}
    for p, w in zip(pattern, words):
        print zip(pattern, words)
        if w not in word and p not in pattern:
            # Build mapping. Space: O(c)
            word[w] = p
            pattern[p] = w 
        elif w not in w2p or w2p[w] != p:
            # Contradict mapping.
            return False
    return True

print wordPattern("abab", "dog cat dog cat")
print wordPattern("aaaa", "dog dog dog dog")
print wordPattern("abab", "cat cat cat cat")