# LeetCode 9: Palindrome Number
# Difficulty: Easy


class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        rev = 0

        while num>0:
            rem=num%10
            num//=10
            rev = rev*10+rem

        return rev==x