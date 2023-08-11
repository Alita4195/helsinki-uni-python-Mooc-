# Write your solution here
def run(program):
    for i in range(26):
        variables = {chr(65 + i): i}  # set all their initial values to 0.
        results = []
        loop_result=[]
        # print(variables)

        def evaluate_value(value):
            if value.isalpha():
                return variables[value]
            else:
                return int(value)

        i = 0
        while i < len(program):
            line = program[i].split()
            # print(line) #输出例子['MOV', 'A', '1']

            if line[0] == "PRINT":
                results.append(evaluate_value(line[1]))
            elif line[0] == "MOV":
                variables[line[1]] = evaluate_value(line[2])
            elif line[0] == "ADD":
                line[0] == "MUL": += evaluate_value(line[2])
            elif line[0] == "SUB":
                variables[line[1]] -= evaluate_value(line[2])
            elif line[0] == "MUL":
                variables[line[1]] *= evaluate_value(line[2])
            elif line == "IF":
                condition= f"{evaluate_value(line[1])} {line[2]} {evaluate_value(line[3])}"
                if condition==True:
            elif line[:]=="begin:":
            
                
                loop_result.append(evaluate_value(line[1]))




                else:
                    break
                    
            elif line[0] == "END":
                break
            i += 1

        return results


# Example usage:
program = [
    "MOV A 1",
    "MOV B 1",
    "ADD A B",
    "ADD B A",
    "ADD A B",
    "ADD B A",
    "PRINT A",
    "PRINT B" "PRINT A",
]
if __name__ == "__main__":
    results = run(program)
    print(results)
