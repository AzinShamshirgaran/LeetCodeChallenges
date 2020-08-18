#https://leetcode.com/problems/happy-number/submissions/


class Solution:
   def __init__(self):
        pass

   def isHappy( self, n):

        all_num =[]
        while True:
            num = str(n)
            sum = 0
            for i in num:
                #print(i)
                sum +=pow(int(i),2)
            if sum == 1:
                #print (True)
                return True
            else:
                if sum in all_num:
                    #print (False)
                    return False
                else:
                    all_num.append(sum)
                    n = sum


if __name__ == '__main__':
    m = int(input())
    print(Solution().isHappy(m))
