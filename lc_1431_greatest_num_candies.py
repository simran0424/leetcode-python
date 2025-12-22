# LeetCode 1431: Kids with greatest Number of candies
# Difficulty: Easy

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = max(candies)
        ans = []

        for currentCandies in candies:
            total_candies = currentCandies + extraCandies
            if total_candies >= maxCandies:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans