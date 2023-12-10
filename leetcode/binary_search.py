from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l < r:

            mid = (l + r) // 2
            # if num in the middle is greater than target
            if nums[mid] > target:
                mid = mid - 1
            elif nums[mid] < target:
                mid = mid + 1
            else:
                return mid

        return -1
