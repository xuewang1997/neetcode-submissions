class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        S, T = {}, {}
        for i in s:
            if i in S: 
                S[i] += 1
            else:
                S[i] = 1
        for j in t:
            if j in T:
                T[j] += 1
            else:
                T[j] = 1
        return S == T
