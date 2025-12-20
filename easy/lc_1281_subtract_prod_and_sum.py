# LeetCode 1281: Subtract the Product and Sum of Digits of an integer
# Difficulty: Easy

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digit = n
        sum = 0
        product = 1

        while digit>0:
            rem = digit%10
            digit//=10
            sum = sum + rem
            product = product * rem

        return product - sum