def twoSum(nums, target):
    n = {}
    for i in range(len(nums)):
        val = target - nums[i]
        if val in n:
            index = n[val]
            print(f"Indexs are {index} and {i}")
            return [index, i]
        n[nums[i]] = i
    print("Not found")
    return -1

nums = [1, 3, 4, 5, 7]
target = 8
twoSum(nums, target)

#T(n) - O(n)
#S(n) - O(n)
