class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ['+','-','*','/']:
                stack.append(i)
            else:
                if i=='+':
                    i = stack.pop()
                    j = stack.pop()
                    stack.append(int(i)+int(j))
                if i=='-':
                    i = stack.pop()
                    j = stack.pop()
                    stack.append(-int(i)+int(j))
                if i=='*':
                    i = stack.pop()
                    j = stack.pop()
                    stack.append(int(i)*int(j))
                if i=='/':
                    i = stack.pop()
                    j = stack.pop()
                    stack.append(int(j)/int(i))
        return int(stack.pop())
                    