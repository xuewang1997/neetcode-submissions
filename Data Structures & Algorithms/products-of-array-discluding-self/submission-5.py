class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        right = 1
        for i in range(1, len(nums)):
            output[i] = nums[i-1]*output[i-1]
        for j in range(len(nums)-2, -1, -1):
            right = right*nums[j+1]
            output[j] = output[j]*right
        return output