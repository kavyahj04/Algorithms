def containsDuplicate(nums):
    hashmap = {}
    for i in range(len(nums)):
        if nums[i] in hashmap:
            print("True")
            return True
        hashmap[nums[i]] = i
    print("False")
    return False

# numbers = [1,2, 4, 5, 7]
numbers = [1,2, 4, 5, 7, 1]

containsDuplicate(numbers)

#TC - O(n)
#SC - O(n) - because we are using hashmap