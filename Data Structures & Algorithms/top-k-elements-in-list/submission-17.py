class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(0, len(nums))]
        nums_count = {}
        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1
        for num, count in nums_count.items():
            buckets[count-1].append(num)
        output = []
        for b in reversed(buckets):
            if b != [] and k > 0:
                output.extend(b)
                k = k - len(b)
        return output