
def strobogrammaticNumber(self, nums):
    dict = { '0': '0', '1': '1', '6': '9', '9': '6', '8':'8'}
    left_pointer = 0
    right_pointer = len(nums)-1

    while left_pointer < right_pointer: 
        if nums[left_pointer] not in dict or dict[left_pointer] != nums[right_pointer]:
            return False
        else:
            left_pointer += 1
            right_pointer -= 1
    return True
