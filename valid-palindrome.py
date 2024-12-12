# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
class Solution:
    def is_alphanumeric(self, c):
        return (c >= "a" and c <= "z") or (c >= "0" and c <= "9")

    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s.lower() if self.is_alphanumeric(c)])
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False

        return True
