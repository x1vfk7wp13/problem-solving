class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parantheses = {')': '(', '}':'{', ']':'['}

        for c in s:
            if c in parantheses.values():
                # opening
                stack.append(c)
            else:
                #closing
                if len(stack) > 0 and stack[-1] == parantheses[c]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
                