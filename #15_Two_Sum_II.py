def twoSum(nums, target):
    l = 0
    r = len(nums) - 1

    while l < r:
        sum_ = nums[l] + nums[r]
        if sum_ < target:
            l += 1
        elif sum_ > target:
            r -=1
        else:
            print(f"{[l+1, r+1]}")
            return [l+1, r+1]

nums = [1,2,4,7]
target = 6
twoSum(nums, target)