"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).
"""

class Solution:
    def guessNumber(self, n: int) -> int:
        if n ==1:
            return 1
        right = n
        left=0
        while left <= right:
            mid=(right+left)//2
            if guess(mid)==0:
                return mid
            elif guess(mid)==1:
                left=mid+1
            else:
                right=mid-1
