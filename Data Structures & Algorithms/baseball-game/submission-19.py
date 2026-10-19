class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        x=0
        for op in operations:
            if op=="+":
                x=stack[-1]+stack[-2]
                stack.append(x)
                #stack.pop()

            elif op=="D":
                x=stack[-1]*2
                stack.append(x)
            elif op=="C":
                stack.pop()
            else:
                stack.append(int(op))
            print(stack)
        return sum(stack)