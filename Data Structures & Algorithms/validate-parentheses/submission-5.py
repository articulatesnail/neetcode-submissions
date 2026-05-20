import re

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen = {
        ")":"(",
        "]":"[",
        "}":"{",
        }
        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                    print(f"stack: {stack}") 
                else:
                    return False

            else:
                stack.append(char)

        return True if not stack else False