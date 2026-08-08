class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for num in tokens:
            if num not in {"+", "-", "*", "/"}:
                stack.append(int(num))
            else:
                num1 = stack.pop()
                num2 = stack.pop()

                if num == "+":
                    result = num2 + num1
                elif num == "-":
                    result = num2 - num1
                elif num == "*":
                    result = num2 * num1
                else:
                    result = int(num2 / num1)

                stack.append(result)

        return stack.pop()