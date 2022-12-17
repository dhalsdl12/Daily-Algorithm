class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        operators = {'+', '-', '*', '/'}

        if len(tokens) == 1: 
            return int(tokens[0])

        for t in tokens:
            if t not in operators:
                result.append(int(t))
            else:
                b = result.pop()
                a = result.pop()

                if t == '+':
                    result.append(a + b)
                elif t == '-':
                    result.append(a - b)
                elif t == '*':
                    result.append(a * b)
                elif t == '/':
                    result.append(int(a / b))

        return result.pop()