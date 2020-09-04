class Solution:
    def plusOne(self, digits):
        n = len(digits)
        if digits == [0]:
            return [1]
        for i in range(n):
            if digits[n-i-1] < 9:
                digits[n - i - 1] += 1
                return digits
            digits[n - i - 1] = 0
        if digits[0] == 0:
            digits.insert(0,1)
            return digits


if __name__ == '__main__':
  S = [9,9,9]



  print(Solution().plusOne(S))