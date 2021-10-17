#Given an array of integers nums, calculate the pivot index of this array.The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal #to the sum of all the numbers strictly to the index's right.

#If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        elif sum(nums[1:])==0:
            return 0


        for i in range(1,len(nums)):
            
            if sum(nums[i+1:])==sum(nums[:i]):
                return i
        return -1
