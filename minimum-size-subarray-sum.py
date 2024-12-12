from typing import List


class Solution:
    # Given an array of positive integers nums and a positive integer target,
    # return the minimal length of a subarray whose sum is greater than or equal to target.
    # If there is no such subarray, return 0 instead.
    # eg: nums=[3,3,1,1,4,1], target=7 => 2
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = sum(nums)
        if total < target:
            return 0

        left = 0
        right = 0
        min = len(nums)
        current = 0
        for i in range(0, len(nums)):
            current += nums[right]
            if current >= target:
                while current >= target:
                    if current - nums[left] >= target:
                        current -= nums[left]
                        left += 1
                    else:
                        break
                if 1 + right - left < min:
                    min = 1 + right - left

            right += 1
            if right >= len(nums):
                break
        return min

    def ___minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min = len(nums) + 1
        for i in range(len(nums)):
            total = 0
            couldnt_find = True
            for j in range(i, len(nums)):
                total += nums[j]
                if total >= target:
                    couldnt_find = False
                    if min > (1 + j - i):
                        min = 1 + j - i
                    break
            if couldnt_find:
                break
        return min if min <= len(nums) else 0

    def _recursive(self, begin, end, current_sum):
        # begin & end are indices into self.nums: begin is inclusive, end is exclusive
        length_of_range = end - begin
        if length_of_range < 1:
            return
        if current_sum >= self.target:
            if length_of_range < self.min:
                self.min = length_of_range
            self._recursive(begin + 1, end, current_sum - self.nums[begin])
            self._recursive(begin, end - 1, current_sum - self.nums[end - 1])
        else:
            return

    def _minSubArrayLen(self, target: int, nums: List[int]) -> int:
        self.target = target
        self.nums = nums
        self.min = len(nums)
        total = sum(nums)
        if total < target:
            return 0

        self._recursive(0, self.min, total)
        return self.min

    def __minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # [2,3,1,2,4,3] => 2
        total = sum(nums)
        if total < target:
            return 0
        nums_order = [
            i[0] for i in sorted(enumerate(nums), key=lambda x: x[1], reverse=True)
        ]
        min = len(nums)
        for index in nums_order:
            current_sum = nums[index]
            current_count = 1
            left = index
            right = index
            while current_count <= min:
                if current_sum >= target:
                    if current_count < min:
                        min = current_count
                    break
                left_item = 0 if left - 1 < 0 else nums[left - 1]
                right_item = 0 if right + 1 >= len(nums) else nums[right + 1]
                if left_item == 0 and right_item == 0:
                    break
                elif left_item >= right_item:
                    current_sum += left_item
                    left = left - 1
                else:
                    current_sum += right_item
                    right = right + 1
                current_count += 1
        return min


print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(Solution().minSubArrayLen(213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]))
