from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ans = nums * 2
        # ans = nums + nums

        return ans


nums = [1, 2, 1]
s = Solution()
print(s.getConcatenation(nums))