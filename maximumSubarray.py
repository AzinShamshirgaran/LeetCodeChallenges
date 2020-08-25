#https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums) :

        sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            sum = max(nums[i], sum)

        return sum

if __name__ == '__main__':
    commands = [4,-1,4,-2,4]

    print(Solution().maxSubArray(commands))