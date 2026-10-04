class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
                continue
            
            if not stack or pairs[char] != stack.pop():
                return False

        return len(stack) == 0