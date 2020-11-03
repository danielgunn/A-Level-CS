operators_precedence = {"+":1,"-":1,"*":2,"/":2}

# e.g 3*2 + 12 / 3 - 17
# answer should be -7
infix_tokens = [3, "*", 2, "+", 12, "/", 3, "-", 17]
print("PREFIX",infix_tokens)

# Shunting-Yard Algorithm
stack = []
postfix_tokens = []
for x in infix_tokens:
    if x in operators_precedence.keys():
        while(stack != [] and (operators_precedence[stack[-1]]>operators_precedence[x])):
            op = stack.pop()
            postfix_tokens.append(op)
        stack.append(x)
    else:
        postfix_tokens.append(x)
while(stack != []):
    op = stack.pop()
    postfix_tokens.append(op)

print("POSTFIX",postfix_tokens)

# Evaluate the RPN
stack=[]
for x in postfix_tokens:
    if x in operators_precedence.keys():
        a = stack.pop()
        b = stack.pop()
        c = 0
        if x == "+":
            c = a + b
        elif x == "-":
            c = b - a
        elif x == "*":
            c = a * b
        else:
            c = b / a
        stack.append(c)
    else:
        stack.append(x)
answer = stack.pop()
print(answer)