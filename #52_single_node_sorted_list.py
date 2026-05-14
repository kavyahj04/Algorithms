def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if(m+1 < len(nums) and nums[m] == nums[m+1]):
                if m % 2 == 0 :
                    l = m + 2
                else:
                    r = m - 1
            elif m > 0 and nums[m] == nums[m - 1]:
                if m % 2 == 0 :
                    r = m - 2
                else:
                    l = m + 1
            else:
                return nums[m]
                