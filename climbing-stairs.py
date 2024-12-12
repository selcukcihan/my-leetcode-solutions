import math


class Solution:
    def climbStairs(self, n: int) -> int:
        ways = 0
        count_of_ones = n
        count_of_twos = 0
        while count_of_ones >= 0:
            current = math.factorial(count_of_twos + count_of_ones) / (
                math.factorial(count_of_twos) * math.factorial(count_of_ones)
            )
            ways += current

            count_of_ones -= 2
            count_of_twos += 1

        return int(ways)
