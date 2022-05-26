# Given a binary array nums, return the maximum number of 
# consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_onepairs = 0
        current_onepairs = 0
        for i in nums:
            if(i == 1):
                current_onepairs+=1
                if(current_onepairs > max_onepairs):
                    max_onepairs = current_onepairs
            else:
                current_onepairs = 0
        print(max_onepairs)
        return max_onepairs