#Write an efficient function that checks whether any permutation of an input string is a palindrome.
def isPermutation(str):
    dict = {}
    for c in str:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    
    odd_pair_seen = False
    for i in dict.values():
        print i
        if i % 2 == 1:
            if odd_pair_seen:
                return False
            
            else:
                odd_pair_seen = True    
    return True
    