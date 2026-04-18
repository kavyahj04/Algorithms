def maxConseq1(nums):
    l = 0
    res = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            l = r + 1
            continue
        res = max(res, r-l+1)
    print(res)
    return res 

nums = [1,1,0,1,1,1]
maxConseq1(nums)