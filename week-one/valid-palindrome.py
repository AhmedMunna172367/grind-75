class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        right, left = len(s) - 1, 0

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[right] != s[left]:
                return False

            right -= 1
            left += 1

        return True
