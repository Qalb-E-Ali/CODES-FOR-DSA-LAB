close_list = ["]", "}", ")"]
open_list = ["[", "{", "("]

def check(aStr): # Function to check parentheses
    stack = []
    for i in aStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "FALSE/Unbalanced"
    if len(stack) == 0:
        return "TRUE/Balanced"
    else:
        return "FALSE/Unbalanced"
#string for the parenthesis check
print("The following program checks if the parenthesis in the string are balanced or not.")
is_balanced = "({a+b})"
print(is_balanced, "-->", check(is_balanced))

is_balanced = "))((a+b}{"
print(is_balanced, "-->", check(is_balanced))

is_balanced = "((a+b))"
print(is_balanced, "-->", check(is_balanced))

is_balanced = "))"
print(is_balanced, "-->", check(is_balanced))

is_balanced = "[a+b]*(x+2y)*{gg+kk}"
print(is_balanced, "-->", check(is_balanced))