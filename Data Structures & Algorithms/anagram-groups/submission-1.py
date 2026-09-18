class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force solutions; most intuitive
        strs_sorted = dict()
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted not in strs_sorted:
                strs_sorted[s_sorted] = [s]
            else:
                strs_sorted[s_sorted].append(s)
        return list(strs_sorted.values())
