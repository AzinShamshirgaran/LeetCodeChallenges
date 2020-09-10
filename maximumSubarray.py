#https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums) :

        sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            sum = max(nums[i], sum)

        return sum

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         sum = nums[0]
#         sum_total = nums[0]
#         for i in range (1, len(nums)):
#             if sum + nums[i] > nums[i]:
#                 sum = sum + nums[i]
#             else:
#                 sum = nums[i]
#             sum_total = max( sum_total, sum)
#         return sum_total

if __name__ == '__main__':
    commands = [4,-1,4,-2,4]

    print(Solution().maxSubArray(commands))