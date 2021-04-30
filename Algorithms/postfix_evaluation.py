from data_structures.stack_array import dynamic_stack

def is_operatore(element):
    if(element in ["+", "-", "*", "/", "^"]):
        return True

    return False

def perform_operation(operator, operand_1, operand_2):
    if(operator == "+"):
        return float(operand_1) + float(operand_2)
    elif(operator == "-"):
        return float(operand_1) - float(operand_2)
    elif(operator == "*"):
        return float(operand_1) * float(operand_2)
    elif(operator == "/"):
        return float(operand_1) / float(operand_2)
    elif(operator == "^"):
        return float(operand_1) ^ float(operand_2)

    return 0

def evaluate(operands_operators_stream):
    stack_size = 2 * len(operands_operators_stream) / 3
    stack = dynamic_stack(stack_size, 5)

    for op in operands_operators_stream:
        if(is_operatore(op) == True):
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            stack.push(perform_operation(op, operand_1, operand_2))
        else:
            stack.push(op)

    return stack.pop()