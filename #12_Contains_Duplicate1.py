def checkDuplicate(nums):
    elements = {}

    for n in nums:
        elements[n] += elements.get(n, 0) + 1
    
    for value in elements.values():
        if value > 1:
            return True
    return False
