import re

class Solution:
    def isValid(self, s: str) -> bool:
        # while "[]" in s or "{}" in s or "()" in s:
        #     s = s.replace('()', "")
        #     s = s.replace('{}', "")
        #     s = s.replace('[]', "")
        # return s==''


        stack=[]
        closeToOpen = {
        ")":"(",
        "]":"[",
        "}":"{",
        }
        for char in s:
            #if c is a closing bracket then check if opening is in top of stack
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                    print(f"stack: {stack}") 
                else:
                    return False
            #if c is open bracket then just add to stack
            else:
                stack.append(char)

        return True if not stack else False