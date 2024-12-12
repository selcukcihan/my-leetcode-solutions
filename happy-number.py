# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum_of_squares_of_digits(number: int) -> int:
            new_number = 0
            while True:
                digit = number % 10
                new_number += digit * digit
                number -= digit
                number = number // 10
                if number == 0:
                    return new_number

        numbers_seen = set()
        while True:
            n = get_sum_of_squares_of_digits(n)
            if n == 1:
                return True
            else:
                if n in numbers_seen:
                    return False
                else:
                    numbers_seen.add(n)
