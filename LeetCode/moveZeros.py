#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# [0,1,2,0,10] == [1,2,10,0,0]

def moveZeros(nums): 
    i = 0
    j = 0
    while j < len(nums):
        if nums[j] == 0:
            j += 1
        else:
            nums[i] = nums[j]
            i += 1
            j += 1
            
    while i < len(nums):
        nums[i] = 0
        i += 1
    return nums
            
            
print moveZeros([0,1,2,0,10])