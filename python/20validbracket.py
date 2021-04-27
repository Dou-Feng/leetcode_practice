class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif not len(stack):
                return False
            else:
                top = stack.pop()
                if (c == ')' and top != '(') or (c == '}' and top != '{') or (c == ']' and top == '['):
                    return False
            
        return len(stack) == 0
                