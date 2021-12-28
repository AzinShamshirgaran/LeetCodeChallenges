"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""

#https://leetcode.com/explore/learn/card/dynamic-programming/631/strategy-for-solving-dp-problems/4045/


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) ==0 or len(text2)==0:
            return 0
        left=right=0
        count =0
        if len(text1) < len(text2):
            while left <len(text1):
                if text1[left] == text2[right]:
                    count +=1
                    right +=1
                    
                else:
                    right +=1
                left +=1
        else:
            while left <len(text2):
                if text2[left] == text1[right]:
                    count +=1
                    right +=1
                    
                else:
                    right +=1
                left +=1
        return count
