from typing import List

# Given an integer array nums sorted in non-decreasing order,
# remove some duplicates in-place such that each unique element appears at most twice.
# The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # example input : 1,1,1,2,2,3,3,3,3,5,5,6,7,7,7
        # example output: 1,1,2,2,3,3,5,5,6,7,7
        current_length = len(nums)
        end_index = current_length - 1

        while end_index > 0:
            # look back fron nums[end_index] until you find an element that is different from nums[end_index]
            new_end_index = end_index - 1
            while new_end_index >= 0 and nums[new_end_index] == nums[end_index]:
                new_end_index -= 1
            # now we need to remove duplicates to ensure at most 2 duplicates
            removal_count = (end_index - new_end_index) - 2
            if removal_count > 0:
                # we should remove "removal_count" elements starting from new_end_index + 1
                for i in range(new_end_index + 1 + removal_count, current_length):
                    nums[i - removal_count] = nums[i]

                current_length -= removal_count
            end_index = new_end_index
        return current_length


s = Solution()
array = [1, 1, 1, 2, 2, 3, 3, 3, 3, 5, 5, 6, 7, 7, 7]
print(s.removeDuplicates(array))
print(array)
