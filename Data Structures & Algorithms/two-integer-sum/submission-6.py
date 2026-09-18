class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            residue = target-num
            for j, num_rest in enumerate(nums):
                if num_rest == residue and i != j:
                    return [i, j]