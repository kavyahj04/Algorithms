#Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Input: nums = [1,2,3,1]

# Output: true

def contains_duplicate(nums):
    nums_map = {}
    for n in nums:
        nums_map[n] = 1 + nums_map.get(n, 0)
    
    for key, value in nums_map.items():
        if value > 1:
            print("True")
            return True
    print("False")
    return False 

nums = [1, 2, 3, 4, 1]
nums = [1, 2, 3, 4]
contains_duplicate(nums)