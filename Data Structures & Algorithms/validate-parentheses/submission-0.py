class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToopen = {')': '(', ']': '[', '}': '{'}

        for symbol in s:
            if symbol in closeToopen:
                if stack and stack[-1] == closeToopen[symbol]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(symbol)
            
        return True if not stack else False
        