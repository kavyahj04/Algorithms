def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l+r) // 2
        #left portion
        if nums[mid] == target:
            print(mid)
            return mid
        if nums[mid] >= nums[l]:

            #can use 2 conditions instead of elif
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[l]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
        else:
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            elif target < nums[r]:
               r = mid - 1
    print(-1)
    return -1 

nums = [4,5,6,7,0,1,2]
target = 2
search(nums, target)