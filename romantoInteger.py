#https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        num = 0
        for i in range(len(s)):
            if i+1 < len(s):

               if s[i] == "I":
                  if s[i + 1] == "V" or s[i + 1] == "X":
                     num -= values [s[i]]
                  else:
                      num +=values [s[i]]


               elif s[i] == "X":

                   if s[i + 1] == "L" or s[i + 1] == "C":
                      num -= values [s[i]]
                   else:
                      num += values [s[i]]

               elif s[i] == "C":
                   if s[i + 1] == "D" or s[i + 1] == "M":
                      num -= values [s[i]]
                   else:
                      num += values [s[i]]
               else:
                   num += values[s[i]]

            else:
                # if s[i] == "I":
                #     num += 1
                # elif s[i] == "X":
                #     num += 10
                # elif s[i] == "C":
                #     num += 100
                # elif s[i] == "V":
                #     num += 5
                # elif s[i] == "D":
                #     num += 500
                # elif s[i] == "L":
                #     num += 50
                # elif s[i] == "M":
                #     num += 1000
                num += values [s[i]]

        return num








if __name__ == '__main__':
    s = "IV"

    print(Solution().romanToInt(s))