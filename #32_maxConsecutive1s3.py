def maxConseq3(nums, k):
    l, res = 0, 0
    count = {}

    for r in range(len(nums)):
        count[nums[r]] = 1 + count.get(nums[r], 0)
        if (r-l+1) - count.get(1, 0) > k:
            count[nums[l]] -= 1
            l += 1
        res = max(res, r-l+1)
    print(res)
    return res 


nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
maxConseq3(nums, k)