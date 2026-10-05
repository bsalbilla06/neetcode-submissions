class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for symbol in tokens:
            try:
                number = int(symbol)
                stack.append(number)
            except:
                num2, num1 = stack.pop(), stack.pop()
                if symbol == '+':
                    stack.append(num1 + num2)
                elif symbol == '-':
                    stack.append(num1 - num2)
                elif symbol == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
        return stack.pop()