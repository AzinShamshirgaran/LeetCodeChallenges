#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
                stack = []
                mapping = {")": "(", "}": "{", "]": "["}
                for char in s:
                    if char in mapping:
                        top_element = stack.pop() if stack else '#'
                        if mapping[char] != top_element:
                            return False
                    else:
                        stack.append(char)

                if not stack:
                    return True




if __name__ == '__main__':
   commands = "{}"

   print(Solution().isValid(commands))