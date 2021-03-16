def arithmetic_arranger(problems, solve=False):
    output = ''
    if(len(problems) > 5):
        return 'Error: Too many problems.'
    for row in range(4):
        for key, problem in enumerate(problems):
            equation = list(problem.split(" "))
            num1, operation, num2 = equation

            # check len of numbers
            if(len(num1) > 4 or len(num2) > 4):
                return "Error: Numbers cannot be more than four digits."

            # check if numbers
            if(not(num1.isdigit() and num2.isdigit())):
                return "Error: Numbers must only contain digits."

            # check operations
            if(not(operation == '+' or operation == '-')):
                return "Error: Operator must be '+' or '-'."

            # check how long per problem
            width = maxlen = max(len(num1), len(num2))+2
            if(key > 0):
                width = maxlen+4

            # operations
            if(row == 0):
                output += '{message: >{width}}'.format(
                    message=num1, width=width)
            if(row == 1):
                output += '{opr: >{opr_width}}{message: >{width}}'.format(
                    opr=operation, message=num2, opr_width=5 if key > 0 else 1, width=maxlen-1)
            if(row == 2):
                output += '{message: >{width}}'.format(
                    message='-'*maxlen, width=width)
            if(solve and row == 3):
                result = 0
                # calculate
                if(operation == '+'):
                    result = int(num1) + int(num2)
                elif(operation == '-'):
                    result = int(num1) - int(num2)

                output += '{message: >{width}}'.format(
                    message=result, width=width)
        output += '' if row == 3 or (row == 2 and solve == False) else '\n'

    return output


print(arithmetic_arranger(
    ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
