    #Optimized Solution
    class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst={}
        for x in range(len(nums)):
            if target-nums[x] in lst:
                return [lst[target-nums[x]], x]
            else:
                lst[nums[x]]=x


class Solution:
    def two_sum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i]+nums[j] == target:
                        res = [i, j]
                        return res
                        break
        return None


if __name__ == '__main__':
    nums = [2, 7, 4, 15]
    target = 9
    test = Solution().two_sum(nums, target)
    print(test)
    
    

