from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        array = [0] * (2 * n)
        for i in range(n):
            array[2 * i] = nums[i]
            array[(2 * i) + 1] = nums[i + n]

        return array


nums = [1, 2, 3, 4, 4, 3, 2, 1]
n = 4

s = Solution()
print(s.shuffle(nums, n))
