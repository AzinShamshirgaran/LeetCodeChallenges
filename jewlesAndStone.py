class Solution:


   def numJewelsInStones(self, J: str, S: str) :
       count = 0
       for i in S:


           if i in J:
               count += 1
       return count


if __name__ == '__main__':
    J = "z"
    S = "ZZZ"
    print(Solution().numJewelsInStones(J, S))