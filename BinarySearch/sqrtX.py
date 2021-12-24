#Given a non-negative integer x, compute and return the square root of x.

#Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        right=x
        left=0
        while left <= right:
            mid=(left+right)//2
            
            if mid*mid==x:
                return mid
            elif mid*mid > x:
                right=mid-1
            else:
                left=mid+1
        return right
         
