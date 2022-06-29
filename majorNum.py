#Given an array nums of size n, return the majority element.The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_dict={}
        for i in range(len(nums)):
            if nums[i] in maj_dict:
                maj_dict[nums[i]] +=1
            else:
                maj_dict[nums[i]] =1
        for key, value in maj_dict.items():
            if value == max(maj_dict.values()):
                return key
