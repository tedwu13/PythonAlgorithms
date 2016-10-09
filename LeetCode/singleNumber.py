Given an array of integers, every element appears twice except for one. Find that single one.


def singleNumber(nums):
    nums.sort()
    for i in range(0, len(nums),2):
        if (i != len(nums) - 1) and (nums[i] != nums[i+1]):
            return nums[i]
        elif i == (len(nums)-1):
            return nums[i]
#[1,1,2,2,3,3,4]
print singleNumber([1,2,1,2,4,3,3])
