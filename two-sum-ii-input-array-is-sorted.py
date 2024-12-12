from typing import List

# Given a 1-indexed array of integers numbers that is already
# sorted in non-decreasing order, find two numbers such that
# they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2,
# added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution.
# You may not use the same element twice.
# Your solution must use only constant extra space.


class Solution:
    def _find(self, numbers: List[int], begin: int, end: int, n: int):
        # begin is included, end is excluded, so the range is => [begin, end)
        if begin >= end:
            return -1
        length = end - begin
        index = begin + length // 2
        if numbers[index] == n:
            return index
        elif numbers[index] < n:
            return self._find(numbers, index + 1, end, n)
        else:
            return self._find(numbers, begin, index, n)

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if i < len(numbers) - 1 and numbers[i] + numbers[i + 1] > target:
                return []
            n = target - numbers[i]
            n_index = self._find(numbers, i + 1, len(numbers), n)
            if n_index != -1:
                return [i + 1, n_index + 1]
        return []

    def twoSum_slow(self, numbers: List[int], target: int) -> List[int]:
        # 1, 4, 5, 10, 13, 15
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []


print(Solution()._find([1, 2, 3, 4, 5], 0, 5, 2))
print(Solution().twoSum([2, 7, 11, 15], 9))
