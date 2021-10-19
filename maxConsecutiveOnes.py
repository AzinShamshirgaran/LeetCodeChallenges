#Given a binary array nums, return the maximum number of consecutive 1's in the array.


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counts=0
        max_counts=0
        for i in range(len(nums)):
            if nums[i] == 1:
                counts += 1
            else:
                max_counts = max(counts,max_counts)
                counts=0
        return max(counts,max_counts)
