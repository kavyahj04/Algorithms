
def maxSubArray(nums):
        #Kadane’s Algorithm
        current = nums[0]
        max_num = nums[0]
        for i in range(1, len(nums)):
            if(current + nums[i] > nums[i]):
                current = current + nums[i]
            else:
                current = nums[i]
            if(current > max_num):
                max_num = current 
        return print(f"maximum sum of sub array is :: {max_num}")

nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(nums)