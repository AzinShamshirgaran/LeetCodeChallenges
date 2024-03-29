#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. #Otherwise, return -1.

#You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        right=len(nums)-1
        left=0
        
        while left <= right:
            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1
