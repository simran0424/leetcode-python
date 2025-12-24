# LeetCode 1523: Count odd numbers in an interval
# Difficulty: Easy

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high+1)//2 - (low)//2
     