# LeetCode 2520: Count the digits that divide a number
# Difficulty: Easy

class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        count = 0
        while temp > 0:
            rem = temp%10
            if num%rem==0:
                count+=1
            temp//=10