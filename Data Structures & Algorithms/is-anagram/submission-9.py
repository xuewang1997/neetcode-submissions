class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        count_s, count_t = [0]*26, [0]*26
        for i, j in zip(s, t):
            count_s[ord(i)-ord('a')] += 1
            count_t[ord(j)-ord('a')] += 1
        return count_s == count_t