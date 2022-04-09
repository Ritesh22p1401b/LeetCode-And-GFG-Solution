class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preview ={}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in preview:
                return [preview[diff],i]
            preview[n] = i               
        return