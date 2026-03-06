def BinarySearch(nums, target):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if(nums[mid] == target):
            return print(f"found target {target} at index {mid}")

        if(nums[mid] < target):
            low = mid + 1
        else:
            high = mid - 1
    return print("Coudn't find the target")

#nums = [1, 2, 3, 4, 5, 6]
nums = [3,5,6,7,9,10]
BinarySearch(nums, 3)            