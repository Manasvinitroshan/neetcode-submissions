class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for num in tokens:
            if num == '+':
                stack.append(stack.pop() + stack.pop())
            elif num == '*':
                stack.append(stack.pop() * stack.pop())

            elif num == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))

            elif num == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)

            else:
                stack.append(int(num))
            




            
        return stack[0]



        

        
