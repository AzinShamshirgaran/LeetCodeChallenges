#https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums) :

        if len(nums) is 0:
            return 0
        elif len(nums) is 1:
            return nums[0]

        sum1 = 0
        sum2 = nums[0]
        for i in range(1, len(nums)):
            tmp = max(nums[i] + sum1, sum2)
            sum1 = sum2
            sum2 = tmp

        return max(sum1, sum2)

if __name__ == '__main__':
    nums = [1,1,1,5]
    print(Solution().rob(nums))