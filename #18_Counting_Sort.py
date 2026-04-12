def countingSort(nums):
    max_val = max(nums)
    count = [0] * (max_val + 1)

    for n in nums:
        count[n] += 1

    k = 0
    for i, freq in enumerate(count):
        for _ in range(freq):
            nums[k] = i
            k+=1
    print(nums)


nums = [2,0,2,1,1,0]
countingSort(nums)


