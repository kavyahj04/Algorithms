def selectionSort(nums):
    new_arr = []
    for i in range(len(nums)):
        smallest_index = findSmallest(nums)
        new_arr.append(nums.pop(smallest_index))
    return print(f"new sorted array is::{new_arr}")


def findSmallest(nums):
    smallest_num = nums[0]
    smallest_index = 0
    for i in range(1, len(nums)):
        if(nums[i] < smallest_num):
            smallest_num = nums[i]
            smallest_index = i
    return smallest_index

nums = [2,9,12,4,7,5,2,3]
selectionSort(nums)