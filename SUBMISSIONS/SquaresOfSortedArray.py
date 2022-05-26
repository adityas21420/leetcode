# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares_list = []
        for i in nums:
            squares_list.append(i*i)
        print("unsorted",squares_list)
        squares_list.sort()
        print("sorted",squares_list)
        return squares_list