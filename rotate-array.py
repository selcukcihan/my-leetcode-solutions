from typing import List

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # input : [1,2,3,4,5,6,7], k = 3
        # output: [5,6,7,1,2,3,4]
        k = k % len(nums)
        l = [x for x in nums]
        for i in range(k):
            nums[i] = l[i + len(l) - k]
        for i in range(len(l) - k):
            nums[i + k] = l[i]
