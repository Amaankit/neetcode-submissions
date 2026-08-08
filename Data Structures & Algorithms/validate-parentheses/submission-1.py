class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            else:
                if stack:
                    if stack[-1] != pairs[i]:
                        return False
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
        