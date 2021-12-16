lines = [
        '[({(<(())[]>[[{[]{<()<>>',
         '[(()[<>])]({[<{<<[]>>(',
         '{([(<{}[<>[]}>{[]{[(<()>',
         '(((({<>}<{<{<>}{[]{[]{}',
         '[[<[([]))<([[{}[[()]]]',
         '[{[{({}]{}}([{[{{{}}([]',
         '{<[[]]>}<{[{[{[]{()[[[]',
         '[<(<(<(<{}))><([]([]()',
         '<{([([[(<>()){}]>(<<{{',
         '<{([{{}}[<[[[<>{}]]]>[]]'
        ]
total_score = 0

def find_closure_error(line : str):

    bracket_pairs = {'{' : '}', '(' : ')', '[' : ']', '<' : '>'}
    points_scoring = {')': 3, ']' : 57, '}': 1197, '>': 25137}
    points = 0
    opened_ones = list()
    
    for index, bracket in enumerate(line):

        if bracket in bracket_pairs:
            # if current bracket exist as a key in bracket pairs than add it to list of oppened brackets
            opened_ones.append(bracket)
        else:
            # if current bracket is not 'opening bracket'
            # check if current closing bracket fits to last elem of opened ones
            if bracket == bracket_pairs.get(opened_ones.pop()):
                pass
            else:
                points = points_scoring.get(bracket)
                print(f'Error! No opened bracket for {bracket} on index {index}, Points: {points}')
                return points
    print('line correct!')
    return points
  
for index, line in enumerate(lines):
    print(f' checking line number {index}: {line}')
    total_score += find_closure_error(line)
    print()
print(f'Total score is: {total_score}')