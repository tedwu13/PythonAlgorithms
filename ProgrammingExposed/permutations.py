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

