#https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote:
            return True
        if not magazine:
            return False
        for i in range(len(ransomNote)):
            #print(i)
            if ransomNote[i] not in magazine:
                return False
            else:
                #print(i)
                ind = magazine.index(ransomNote[i])
                magazine = magazine[:ind] + magazine[ind + 1:]
                #print(magazine)
        return True


if __name__ == '__main__':
    ran = "aa"
    mag = "baa"
    print(Solution().canConstruct(ran, mag))