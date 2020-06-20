class Solution(object):
    def isValid(self, s):
        stack = []
        opening = ['(', '{', '[']
        closed = [')', '}', ']']
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if len(stack) != 0 and stack[-1] == opening[closed.index(i)]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
