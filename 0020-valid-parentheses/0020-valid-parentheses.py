class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map.values():  # If it's an opening bracket
                stack.append(char)
            elif char in bracket_map:  # If it's a closing bracket
                if not stack or stack.pop() != bracket_map[char]:
                    return False
        
        # If the stack is empty, all brackets were matched correctly
        return not stack