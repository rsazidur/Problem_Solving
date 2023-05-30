from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            value = nums[nums[i]]
            ans.append(value)

        return ans


nums = [0, 2, 1, 5, 3, 4]

s = Solution()
print(s.buildArray(nums))
