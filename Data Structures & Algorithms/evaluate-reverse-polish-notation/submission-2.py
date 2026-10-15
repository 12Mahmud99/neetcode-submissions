class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations=["+","-","/","*"]
        def operation_result(sign, a , b) -> int:
            if sign == "+":
                return a+b
            if sign == "-":
                return a-b
            if sign == "*":
                return a*b
            if sign == "/":
                return a/b
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in operations:
                stack.append(tokens[i])
            else: 
                result=operation_result(tokens[i],int(stack[-2]),int(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(result)

        return int(stack[-1])
