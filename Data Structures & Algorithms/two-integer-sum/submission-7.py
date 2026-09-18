class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}
        for i, num in enumerate(nums):
            residue = target - num
            if residue in seen_nums:
                return [seen_nums[residue], i]
            else:
                seen_nums[num] = i