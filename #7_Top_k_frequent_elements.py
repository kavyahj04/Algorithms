def topKFrequent(nums, k):
    count = {}

    #need elements from 0 to len(nums) 
    f_elements = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    
    for key, value in count.items():
        f_elements[value].append(key)
    
    new_arr = []
    for i in range(len(nums), -1, -1):
        for elem in f_elements[i]:
            new_arr.append(elem)
            if len(new_arr) == k:
                print(f"{new_arr}")
                return new_arr

nums = [1,1,1,2,2,3]
k = 2
topKFrequent(nums, k)