from typing import List


# Given an integer array nums and an integer k,
# return true if there are two distinct indices
# i and j in the array such that
# nums[i] == nums[j] and abs(i - j) <= k.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map_indices = {}
        for idx, num in enumerate(nums):
            if num in map_indices:
                current_list = map_indices[num]
                current_list.append(idx)
                for i in range(0, len(current_list) - 1):
                    if current_list[i + 1] - current_list[i] <= k:
                        return True
            else:
                map_indices[num] = [idx]

        return False
