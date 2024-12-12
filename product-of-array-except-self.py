# Given an integer array nums, return an array answer
# such that answer[i] is equal to the product of
# all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List


class Solution:
    def __recursive(self, index, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return nums[0] * self._recursive(index + 1, nums[1:])

    def _productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = []
        for i in range(len(nums)):
            answers.append(self._recursive(i, nums[:i] + nums[i + 1 :]))
        return answers

    def __productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        answers = []
        total = 1
        zero_indices = []
        for i in range(len(nums)):
            if nums[i] != 0:
                total *= nums[i]
            else:
                zero_indices.append(i)
        if len(zero_indices) > 1:
            return [0 for x in nums]
        if len(zero_indices) == 1:
            return [0 if x != 0 else total for x in nums]
        for i in range(len(nums)):
            answers.append(total // nums[i])
        return answers

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]

        # output: [1, 1, 2, 6]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        # output: [1, 1, 2, 6], right=4
        # output: [1, 1, 8, 6], right=12
        # output: [1, 12, 8, 6], right=24
        # output: [24, 12, 8, 6], right=24
        return output


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
print(s.productExceptSelf([-1, 1, 0, -3, 3]))
print(s.productExceptSelf([0, 2, 3, 4]))
