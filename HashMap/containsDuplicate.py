#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==0:
            return False
        hashMap={}
        for i in nums:
            if i in hashMap:
                return True
            else:
                hashMap[i]=1
        return False
