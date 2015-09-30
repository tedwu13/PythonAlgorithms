class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        length = len(num)
        if length == 0: return []
        if length == 1: return [num]
        res = []
        for i in range(length):
            for sub in self.permute(num[0:i] + num[i+1:]):
                res.append([num[i]] + sub)
        return res



 For example, [1,2,3] 



def permutations(str_):
    """ Return a generator of all the permutations of the string. """

    # A string such as 'a' has itself as its only permutation, while for 'ab'
    # the permutations are 'ab' and 'ba'. For 'abc', a three-character string,
    # there are six permutations: 'abc', 'acb', 'bac', 'bca', 'cab', 'cba'. Two
    # of these permutations, 'abc' and 'acb', start with 'a', and what follows
    # this first character is, respectively, 'bc' and 'cb': the two possible
    # permutations of 'cb'. This allows us to see the pattern here: for each
    # letter in the string we need to concatenate to it the sub-permutations
    # that can be generated when the letter is removed from the string.

    if len(str_) == 1:
        yield str_

    for index, letter in enumerate(str_):
        # The string without the index-th letter
        without = str_[:index] + str_[index + 1:]
        for sub_permutation in permutations(without):
            yield letter + sub_permutation