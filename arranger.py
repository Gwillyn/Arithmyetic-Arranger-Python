def arithmetic_arranger(problems, show_answers=False):
    
    # Error: if amount of problems given is greater than 5
    if len(problems) > 5: 
        return 'Error: Too many problems.'
    
    # separate equation into operators
    operators = []
    for i in problems: 
        p = i.split()
        operators.extend([p[1]])
    # Error: check if operators match only '+' and '-'
    if not all(map(lambda x: x == '+' or x=='-', operators)):
        return "Error: Operator must be '+' or '-'."
    # Error: separate equation into parts of individuals
    numbers = []
    for i in problems: 
        p = i.split()
        numbers.extend([p[0], p[2]])
    # Error: check if numbers are digits 
    if not all(map(lambda x: x.isdigit(), numbers)):
        return 'Error: Numbers must only contain digits.'
    # Error: check if numbers are greater than 4
    if not all(map(lambda x: len(x) < 5, numbers)):
            return 'Error: Numbers cannot be more than four digits.'


    # equates the solutions to the problems and saves them in a list.
    solutions = []
    for i in problems:
        p = i.split()
        if p[1] == '+':
            solution = int(p[0]) + int(p[2])
            solutions.append(solution)
        elif p[1] == '-':
            solution = int(p[0]) - int(p[2])
            solutions.append(solution)
    
    
    top = ""
    bottom = ""
    line = ""
    solution = ""
    arranged_problem = []
    solution_item = 0
    for i in problems:
        first_number = i.split()[0]
        operator = i.split()[1]
        last_number = i.split()[2]
        # distance of biggest number +2 (+2 for the operator position)
        distance = max(len(first_number), len(last_number)) + 2
        top = top + first_number.rjust(distance) + "    "
        bottom = bottom + operator + last_number.rjust(distance - 1) + "    "
        line = line + "-"*distance + "    "
        solution = solution + str(solutions[solution_item]).rjust(distance) + "    "
        solution_item += 1
    if show_answers == True:
        return f'{top}\n{bottom}\n{line}\n{solution}'
    else: 
        return f'{top}\n{bottom}\n{line}'
    
    
        


print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"], True))
