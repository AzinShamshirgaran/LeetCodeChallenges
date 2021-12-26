# Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        
        max_count=0
        for num in nums:
            if num==1:
                count +=1
            else:
                
                if max_count < count:
                    max_count=count
                count=0
        if max_count < count:
                    max_count=count
        return max_count
