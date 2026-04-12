def maxArea(height):

    #brute force approcah 
    # max_area = 0
    # for l in range(height):
    #     for r in range(l+1, height):
    #         area = (r - l) * min(height[l], height[r])
    #         max_area = max(max_area, area)
    # return max_area

    #optimal solution O(n)
    res = 0
    l = 0
    r = len(height) - 1

    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)
        if height[l] < height[r]:
            l+=1
        else:
            r-=1
    print(res)
    return res


height = [1,8,6,2,5,4,8,3,7]
maxArea(height)