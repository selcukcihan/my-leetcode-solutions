from typing import List


# You are given an integer array nums.
# You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
class Solution:
    def __init__(self):
        self.reachable = False
        self.nums = []

    def _recursive(self, index, memo):
        memo.add(index)
        if index == len(self.nums) - 1:
            self.reachable = True
            return True
        if len(self.nums) == 0:
            return False
        current = self.nums[index]
        for i in range(index + 1, index + current + 1):
            if i < len(self.nums):
                if i not in memo:
                    if self._recursive(i, memo):
                        return True
            else:
                break
        return False

    def canJump(self, nums: List[int]) -> bool:
        self.reachable = False
        self.nums = nums
        self._recursive(0, set())
        return self.reachable
        # [1,1,1,1]
        # [3, 2, 1, 2, 3]
        # [2,3,1,1,4]
