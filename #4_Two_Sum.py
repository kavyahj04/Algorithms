def twoSum(nums, target):
    elements = {}
    indexes = []
    for i in range(len(nums)):
        value = target - nums[i]
        if value in elements:
            indexes.append(elements[value])
            indexes.append(i)
            break
        elements[nums[i]] = i
    print(f"Found indexes at : {indexes}")
    return indexes

nums = [1, 3, 4, 5, 7]
target = 8
twoSum(nums, target)

#T(n) - O(n)
#S(n) - O(n)