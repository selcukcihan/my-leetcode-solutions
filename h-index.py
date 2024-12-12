from typing import List


# Given an array of integers citations where
# citations[i] is the number of citations a researcher received for their ith paper,
# return the researcher's h-index.
# According to the definition of h-index on Wikipedia:
# The h-index is defined as the maximum value of h
# such that the given researcher has published
# at least h papers that have each been cited at least h times.


class Solution:
    def _brute_force(self, citations: List[int]):
        last_h = 0
        for h in range(1, len(citations) + 1):
            count = 0
            for c in citations:
                if c >= h:
                    count += 1
            if count >= h:
                last_h = h

        return last_h

    def _smart(self, citations: List[int]):
        citations = sorted(citations)
        # [0, 1, 3, 5, 6]
        # [7, 6, 5, 4, 3, 0, 0, 1, 0, 2]
        # [0, 0, 0, 1, 2, 3, 4, 5, 6, 7]
        # [0, 0, 0, 0, 0, 1, 1, 1, 100, 101]
        # [1, 1, 3]
        last_h = 0
        for i in range(len(citations) - 1, -1, -1):
            if citations[i] >= last_h + 1:
                last_h += 1
            else:
                break
        return last_h

    def hIndex(self, citations: List[int]) -> int:
        # [3,0,6,1,5]
        return self._smart(citations)


print(Solution().hIndex([1]))
