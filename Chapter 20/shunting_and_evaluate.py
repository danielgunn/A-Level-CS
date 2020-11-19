class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        #print("push called:", data)
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

operators_precedence = {"+":1,"-":1,"*":2,"/":2, ")":0, "(":0}

line_in = input("Please input a math expression with spaces seperating all tokens:")

infix_tokens = line_in.split()
#print("PREFIX",infix_tokens)

# Shunting-Yard Algorithm
operator_stack = Stack()
postfix_tokens = []
depth = 0  # how many layers deep of brackets are we?
for x in infix_tokens:
    #print("Token:",x)
    if x in operators_precedence.keys():
        if x == "(":
            depth += 1
            operator_stack.push(x)
        elif x == ")":
            while (not operator_stack.is_empty()):
                op = operator_stack.pop()
                if op == "(":
                    depth -= 1
                    break
                else:
                    postfix_tokens.append(op)
        else:
            while((not operator_stack.is_empty()) and (operators_precedence[operator_stack.peek()] > operators_precedence[x])):
                op = operator_stack.pop()
                if op not in ("(",")"):
                    postfix_tokens.append(op)
            operator_stack.push(x)
    else:
        postfix_tokens.append(x)
        #print("add3",x)
while(not operator_stack.is_empty()):
    op = operator_stack.pop()
    if op not in ("(",")"):
        postfix_tokens.append(op)

print("POSTFIX",postfix_tokens)

# Evaluate the RPN
operator_stack=[]
for x in postfix_tokens:
    if x in operators_precedence.keys():
        a = float(operator_stack.pop())
        b = float(operator_stack.pop())
        c = 0
        if x == "+":
            c = a + b
        elif x == "-":
            c = b - a
        elif x == "*":
            c = a * b
        else:
            c = b / a
        operator_stack.append(c)
    else:
        operator_stack.append(x)
answer = operator_stack.pop()
print(answer)