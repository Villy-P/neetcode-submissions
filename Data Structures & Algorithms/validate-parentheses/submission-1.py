class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['[', '{', '(']:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                c = stack.pop()
                if (c == '[' and i != ']' or
                   c == '(' and i != ')' or
                   c == '{' and i != '}'):
                   return False
        return len(stack) == 0