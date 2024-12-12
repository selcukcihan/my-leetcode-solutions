from typing import List

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequencies = {}
        max = 0
        element = None
        for n in nums:
            prev = frequencies.get(n)
            val = prev + 1 if prev else 1
            frequencies[n] = val
            if max < val:
                max = val
                element = n
        return element
