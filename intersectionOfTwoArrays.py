#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict={}
        res=[]
        for num1 in nums1:
            if num1 not in dict:
                dict[num1]=1
        for num2 in nums2:
            if num2 in dict:
                dict[num2]=2
        for key, value in dict.items():
            if value ==2:
                res.append(key)
        return res
        
