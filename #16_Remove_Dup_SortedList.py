def removeDuplicates(nums):
    k = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[k]:
            continue
        else:
            k += 1
            nums[k] = nums[i]
            
    #index starts from 0 so +1
    print(k + 1)
    return k + 1

nums = [1,1,1,2,3,4,4,5,6,6,7]
removeDuplicates(nums)