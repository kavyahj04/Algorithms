class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def capCheck(c):
            s, d = 0, 1
            for i in range(len(weights)):
                if s + weights[i] <= c:
                    s += weights[i]
                else:
                    s, d = 0, d + 1
                    s += weights[i]
            if d <= days:
                return True
            else:
                return False
        
        min_cap = max(weights)
        max_cap = sum(weights)
        cap = False
        res = min_cap
        while min_cap <= max_cap:
            mid = (min_cap + max_cap) // 2
            cap = capCheck(mid)
            if cap:
                res = mid
                max_cap = mid - 1
            else:
                min_cap = mid + 1
        return res