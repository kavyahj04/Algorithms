def findsub(nums, k):
    count = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if(sum == k):
                count += 1
    print(f"count is {count}")
    return count

nums = [1, 1, 1]
findsub(nums, 2)