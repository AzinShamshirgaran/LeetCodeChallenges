#https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        stack_S= list(S)
        stack_T = list(T)
        stack_S_F =[]
        stack_T_F = []

        for char in stack_S:
            if char != '#':
                stack_S_F.append(char)
            else:
                if stack_S_F:
                    stack_S_F.pop()
        for char in stack_T:
            if char != '#':
                stack_T_F.append(char)
            else:
                if stack_T_F:
                    stack_T_F.pop()




        if stack_S_F==stack_T_F:
            return True
        return False

if __name__ == '__main__':
   S="ab##"

   T="c#d#"

   print(Solution().backspaceCompare(S,T))