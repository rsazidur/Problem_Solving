from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]


nums = [2, 7, 11, 15]
target = 9

s = Solution()
print(s.twoSum(nums, target))
