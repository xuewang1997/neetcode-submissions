class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = dict()
        for num in nums:
            if num in nums_count:
                nums_count[num] += 1
            else:
                nums_count[num] = 1
        top_k_freq = sorted(nums_count.items(), key=lambda x: x[-1], reverse=True)[:k]
        res = []
        for i in top_k_freq:
            res.append(i[0])
        return res
