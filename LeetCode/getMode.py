[1,2,3,2,2,2,2,2,2,2]
return 2
def getMode(nums):
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return nums[0]
    else:
        sorted_nums = sorted(nums)
        mode = None
        prevNum = None
        count = 0
        maxCount = 0
        for currentNum in nums:
            if currentNum == prevNum:
                count += 1
            if count > maxCount
                maxCount = count
                