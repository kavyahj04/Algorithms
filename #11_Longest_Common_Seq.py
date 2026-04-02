def longest_common_seq(nums):
    nums_Set = set(nums)
    longest_sub = 0
    

    for n in nums:
        #check if this number is start of the sequence
        if (n-1) not in nums_Set:
            length = 0
            while n + length in nums_Set:
                length += 1
            longest_sub = max(longest_sub, length)
    print(f"Longest common sequence is :: {longest_sub}")
    return longest_sub

nums = [100,1,2,3,4,5,23,255,1234]
nums = [9,1,4,7,3,-1,0,5,8,-1,6]
longest_common_seq(nums)