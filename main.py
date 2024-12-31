#!/bin/python3

x = "(()(()a)a(()))(()a)()" #input

C = [] # list of parentheses pairs
c = [] # stack for C
# the reason why a stack is used is because parentheses are interpreted in a FILO kinda way

for i in range(len(x)):
    match x[i]:
        case '(':
            c.append(i) # push
        case ')':
            C.append([c.pop(), i]) # pop
        case _:
            pass

# extra (: c won't be empty
# extra ): c.pop() raises error
C.sort(key=lambda x:x[0])
print(C)