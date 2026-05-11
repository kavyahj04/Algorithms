def nextGreaterII(nums):
    stack = []
    res = [-1] * len(nums)
    n = len(nums)

    for i in range(2 * n):
        while stack and nums[i % n] > stack[-1]:
            popped = stack.pop()
            res[popped] = nums[i % n]
        if i < n:
            stack.append(i)
    print(res)
    return res

nums = [1,2,3,4,3]
nextGreaterII(nums)