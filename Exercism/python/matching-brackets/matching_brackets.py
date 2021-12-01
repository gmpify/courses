def is_paired(input_string):
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    control_stack = []

    for bracket in input_string:
        if bracket in brackets.values():
            control_stack.append(bracket)
        elif bracket in brackets:
            if (len(control_stack) == 0) or (brackets[bracket] != control_stack.pop()):
                return False

    if len(control_stack) != 0:
        return False

    return True
