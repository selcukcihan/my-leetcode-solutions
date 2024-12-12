from typing import List


# There are n children standing in a line.
# Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.


class Solution:
    def _compare_index_and_adjust(self, ratings, candies, i):
        there_are_violations = False
        # compare with left neighbor
        if i > 0:  # has a left neighbor
            if ratings[i] > ratings[i - 1]:
                if candies[i - 1] >= candies[i]:
                    candies[i] = candies[i - 1] + 1
                    there_are_violations = True
        # then compare with right neighbor
        if i < len(ratings) - 1:  # has a right neighbor
            if ratings[i] > ratings[i + 1]:
                if candies[i + 1] >= candies[i]:
                    candies[i] = candies[i + 1] + 1
                    there_are_violations = True
        return there_are_violations

    def candy_slow(self, ratings: List[int]) -> int:
        candies = [1 for x in range(len(ratings))]
        iterations = 0
        there_are_violations = True
        while there_are_violations:
            there_are_violations = False
            for i in range(len(ratings)):
                iterations += 1
                if self._compare_index_and_adjust(ratings, candies, i):
                    there_are_violations = True
        print(iterations)
        return sum(candies)

    def candy_fast(self, ratings: List[int]) -> int:
        sorted_ratings = [i[0] for i in sorted(enumerate(ratings), key=lambda x: x[1])]
        candies = [1 for x in range(len(ratings))]
        iterations = 0
        there_are_violations = True
        while there_are_violations:
            there_are_violations = False
            for _i in range(len(ratings)):
                i = sorted_ratings[_i]
                iterations += 1
                if self._compare_index_and_adjust(ratings, candies, i):
                    there_are_violations = True
        print(iterations)
        return sum(candies)


Solution().candy_slow([x for x in range(2000, 0, -1)])
Solution().candy_fast([x for x in range(2000, 0, -1)])
