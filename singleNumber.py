#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

#You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict={}
        for num in nums:
            if num in dict:
                dict[num]=2
            else:
                dict[num]=1
        for key, value in dict.items():
            if value==1:
                return key
        
