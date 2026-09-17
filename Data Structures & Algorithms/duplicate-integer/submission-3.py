class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use sort() to check the adjacent values are the same or not
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False  