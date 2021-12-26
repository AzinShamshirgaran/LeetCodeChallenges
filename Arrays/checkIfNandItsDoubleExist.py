# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        lst=[]
        for x in arr:
            if 2*x in lst or x/2 in lst:
                return True
            else:
                lst.append(x)
        return False
