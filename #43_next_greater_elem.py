def nextGreater(nums1, nums2):
    mapping, stack = {}, []
    res = []
    for i in range(len(nums2)):
        while stack and nums2[i] > stack[-1]:
            popped = stack.pop()
            mapping[popped] = nums2[i]
        stack.append(nums2[i])
    
    for s in stack:
        mapping[s] = -1
    
    for n in nums1:
        res.append(mapping[n])
    print(res)
    return res

nums1 = [4,1,2]
nums2 = [1,3,4,2]
nextGreater(nums1, nums2)