class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        queue = []
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                num1 = int(queue.pop())
                num2 = int(queue.pop())
                if token == "+":
                    num = num1 + num2
                elif token == "-":
                    num = num2 - num1
                elif token == "*":
                    num = num1 * num2
                else:
                    num = num2 / num1
                queue.append(num)
            else:
                queue.append(token)

        return int(queue.pop())