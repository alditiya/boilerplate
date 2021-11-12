import re

def arithmetic_arranger(problems, show_asnwer=False):
    if len(problems) > 5:
        return "Error; Too many problems."

    lengths = []
    top_operands = []
    bot_operands = []
    operators = []

    for problem_str in problems:
        problem = re.split("([+-/*])", problem_str.replace(" ", ""))

        if not problem[0].isnumeric() or not problem[2].isnumeric():
            return "Ërror: Numbers must only contain digits."

        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if problem[1] != "+" and problem[1] != "-":
            return "Error: Operator must be '+' or '-'."

        lengths.append(max(len(problem[0]), len(problem[2])) + 2)
        top_operands.append(problem[0])
        bot_operands.append(problem[2])
        operators.append(problem[1])
        
    arranged_problems = ""
    for i in range(0, len(lengths)):
        if i > 0:
            arranged_problems += "    "
        arranged_problems += ("-" * lengths[i])

    if show_asnwer:
        arranged_problems += "\n"
        for i in range(0, len(lengths)):
            if i > 0:
                arranged_problems += "    "
            top = int(top_operands[i])
            bot = int(bot_operands[i])
            ans = top + bot if operators[i] == "+" else top - bot

            ans = str(ans)
            arranged_problems += (" " * (lengths[i] - len(ans)))
            arranged_problems += ans


    return arranged_problems