def findNum(nums):
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = -abs(nums[index])
    new_arr = []
    for i in range(len(nums)):
        if(nums[i] > 0):
            new_arr.append(i+1)
    print(new_arr)
    return new_arr

nums = [4,3,2,7,8,2,3,1]
findNum(nums)