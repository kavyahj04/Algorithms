def productOfArray(nums):
    prefix = []
    postfix = []

    prefix_prod = 1
    postfix_prod = 1

    for i in range(len(nums)):
        prefix.append(prefix_prod)
        prefix_prod *= nums[i]

    for i in range(len(nums)-1, -1, -1):
        postfix.append(postfix_prod)
        postfix_prod *= nums[i]

    new_arr = []
    for i in range(len(nums)):
        product = prefix[i] * postfix[len(nums)-1-i]
        new_arr.append(product)
    print(f"{new_arr}")
    return new_arr

nums = [-1,1,0,-3,3]
productOfArray(nums)
