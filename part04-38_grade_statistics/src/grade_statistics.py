def input_info():
    score = []
    while True:    
        input_info = input("Exam points and exercises completed: ")
        if input_info == "":
            print("Statistics: ")
            break

        split_input = input_info.split(" ")  # splits a string into a list
        for i in split_input:
            score.append(int(i))
    return score

def score_num(score: list):
    index = 0
    exercise_points = []
    exam_score_list = []
    for j in score:        
        if index % 2 != 0:
            integer = j // 10
            index += 1
            exercise_points.append(integer)
        else:
            exam_score_list.append(j)
            index += 1

    return exam_score_list, exercise_points

def calculate_sum(exam_score_list: list, exercise_points: list):
    sum_list = []
    for index, item in enumerate(exercise_points):
        sum_list.append(item + exam_score_list[index])
    return sum_list

def calculate_average(sum_list: list):
    average_score = sum(sum_list) / len(sum_list)
    print(f"Points average: {average_score}")

def calculate_pass_percent(sum_list: list, exam_score_list: list):
    pass_num = 0
    for x in exam_score_list:
        if x > 10:
            pass_num += 1
    pass_percentage = pass_num / len(sum_list)*100
    print(f"Pass percentage: {pass_percentage:.1f}")


# 光标选中想要注释的所有代码，ctrl+/，取消同理。
def print_grade_distribution(sum_list: list):
    print("Grade distribution: ")  
    for item in sum_list: 
        sign = ""
        if 28 <= item <= 30:
            sign += "*"
        print(f"5: {sign}")
        
        if 24 <= item <= 27:
            sign += "*"
        print(f"4: {sign}")
        if 21 <= item <= 23:
            sign += "*"
        print(f"3: {sign}")
        if 18 <= item <= 20:
            sign += "*"
        print(f"2: {sign}")
        if 15 <= item <= 17:
            sign += "*"
        print(f"1: {sign}")
        if 0 <= item <= 14:
            sign += "*"
        print(f"0: {sign}")


score = input_info()
score_result = score_num(score)
sum_list = calculate_sum(*score_result)
calculate_average(sum_list)
calculate_pass_percent(sum_list, score_result[0])
print_grade_distribution(sum_list)









