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
        
    


    return problems, solutions 


print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])}')
