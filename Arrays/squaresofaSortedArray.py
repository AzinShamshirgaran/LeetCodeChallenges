#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[]
        left=0
        right=len(nums)-1
        while left<=right:
            if abs(nums[left])<=abs(nums[right]):
                res.insert(0,nums[right]*nums[right])
                right -=1
            else:
                res.insert(0,nums[left]*nums[left])
                left +=1
        return res
