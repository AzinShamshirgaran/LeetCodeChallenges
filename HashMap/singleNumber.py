# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        map={}
        for i in nums:
            if i in map:
                map[i]=2
            else:
                map[i]=1
        for key,val in map.items():
            if val == 1:
                return key
        
