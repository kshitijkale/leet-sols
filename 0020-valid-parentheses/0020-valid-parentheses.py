class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i=='(' or i=='{' or i=='[': stack.append(i)
            if i == ')':
                if(len(stack)!=0):
                    j = stack.pop()
                    if(j!='('):
                        return False
                else:
                    return False
            if i == '}':
                if(len(stack)!=0):
                    j = stack.pop()
                    if(j!='{'):
                        return False
                else:
                    return False
            if i == ']':
                if(len(stack)!=0):
                    j = stack.pop()
                    if(j!='['):
                        return False
                else:
                    return False
        if(len(stack)!=0):
            return False
        return True
            