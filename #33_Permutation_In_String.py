def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_freq = {}
        s2_freq = {}
        win_len = len(s1)
        
        for s in s1:
            s1_freq[s] = 1 + s1_freq.get(s, 0)
        
        for s in range(len(s1)):
            s2_freq[s2[s]] = 1 + s2_freq.get(s2[s], 0)
        
        for r in range(len(s1), len(s2)):
            if s1_freq == s2_freq:
                return True
            s2_freq[s2[r]] = 1 + s2_freq.get(s2[r], 0)
            s2_freq[s2[r - win_len]] -= 1
            if s2_freq[s2[r - win_len]] == 0:
                del s2_freq[s2[r - win_len]]
        
        if s1_freq == s2_freq:
            return True
        return False

s1 = "ab"
s2 = "eidbaooo"
checkInclusion(s1, s2)