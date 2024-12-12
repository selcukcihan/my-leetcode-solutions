from typing import List


# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges
# that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges,
# and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def add_to_result(numbers, res):
            if len(numbers) == 0:
                return
            elif len(numbers) == 1:
                res.append(str(numbers[0]))
            else:
                res.append(f"{numbers[0]}->{numbers[-1]}")

        result = []
        current = []
        for n in nums:
            if len(current) == 0:
                current.append(n)
            else:
                if n == current[-1] + 1:
                    current.append(n)
                else:
                    add_to_result(current, result)
                    current = [n]
        if len(current) > 0:
            add_to_result(current, result)

        return result
