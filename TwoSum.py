class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i, n in enumerate(nums):
            if target - nums[i] in numsDict:
                return [numsDict[target-nums[i]], i]
            else:
                numsDict[n] = i