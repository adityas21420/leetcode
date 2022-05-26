# Given an array nums of integers, 
# return how many of them contain an even number of digits.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_no_digits = []
        for i in nums:
            if(len(str(i))%2 == 0):
                even_no_digits.append(i)
        return len(even_no_digits)
            