class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        check_dict = dict()
        for i, j in zip(s, t):
            if i not in check_dict: 
                check_dict[i] = 1
            else:
                check_dict[i] += 1 
            if j not in check_dict:
                check_dict[j] = -1
            else:
                check_dict[j] -= 1
        for value in check_dict.values():
            if value != 0:
                return False
        return True
