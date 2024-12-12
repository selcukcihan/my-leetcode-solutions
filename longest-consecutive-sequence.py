from typing import List


# Given an unsorted array of integers nums,
# return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers_set = set(nums)
        visited = set()

        def get_consecutive_numbers_including(numbers, current):
            if current in visited:
                return 0
            visited.add(current)
            count = 1
            _current = current - 1
            while _current in numbers_set:
                visited.add(_current)
                count += 1
                _current -= 1
            _current = current + 1
            while _current in numbers_set:
                visited.add(_current)
                count += 1
                _current += 1
            return count

        result = 0
        for n in nums:
            count = get_consecutive_numbers_including(nums, n)
            result = max(result, count)
        return result
