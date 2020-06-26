from stack import Stack


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def checkBalancedParenthesis(parent_string):
    s = Stack()
    is_balanced = True
    index = 0
    while index < len(parent_string) and is_balanced:
        cur_parenthesis = parent_string[index]
        if cur_parenthesis in "({[":
            s.push(cur_parenthesis)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, cur_parenthesis):
                    is_balanced = False

        index += 1

    if(s.is_empty() and is_balanced):
        return True
    else:
        return False


print(checkBalancedParenthesis("([{}])"))
