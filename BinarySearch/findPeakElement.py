"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==0:
            return -1
        if len(nums)==1:
            return 0

        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return len(nums)-1
        right=2
        left=0
        while left <= right and right <len(nums):
            mid=(right+left)//2
            if nums[mid]>nums[right] and nums[mid]>nums[left]:
                return mid
            else:
                
                right +=1
                left +=1
        if mid == len(nums) and nums[mid]>nums[right]:
            return mid
        else:
            return -1
