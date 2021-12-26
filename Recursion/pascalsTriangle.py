# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3234/


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex ==0:
            return [1]
        return self.compute_PT(rowIndex)
    def compute_PT(self, n):
        if n==1:
            return [1,1]
        res=[1]*(n+1)

        temp=self.compute_PT(n-1)
        for i in range (1,n):
            res[i]=temp[i-1]+temp[i]
        return res
        
