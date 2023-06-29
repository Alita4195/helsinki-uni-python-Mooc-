# tee ratkaisu tänne
# student_info = input("Student information: ")
# exercise_data = input("Exercises completed: ")
# exam_point = input("Exam points: ")
# course_info=input("Course information: ")

student_info = "students1.csv"
exercise_data = "exercises1.csv"
exam_point = "exam_points1.csv"
course_info="course1.txt"

def old_course_info2(filename):
    with open(filename) as file:
        current_line = ""
        index=0
        for line in file:
            line = line.strip()
            line=line.split(": ")
            line=line[1]
            if index==0:
                current_line+=f"{line}, "
            if index==1:
                current_line+=line
            index+=1
        print(current_line+" credits")

# old_course_info2(course_info)

        #     if current_line: #True
        #         current_line += ", " + line[-1]+ " credits"

        #     else: #Since current_line is initially an empty string, the else part is executed. 
        #         current_line = line[-1]
        # return(current_line)

# The re-implemented func course_info2(), workable
def course_info2(filename):

    with open(filename) as file:
        result = ""
        for i,line in enumerate(file):
            result=result + line.strip().split(": ", 1)[1] #setting the maxsplit parameter to 2, will return a list with 2 elements!
            if i ==0: result+=", "   
        print(result +" credits")
#小吴        
course_info2(course_info)    

def sign():
    result="======================================"
    return result

# def course_info2(filename):
#     with open(filename) as file:
#         current_line=""
#         for line in file:
#             #line=line.replace("\n","") #remove 空行
#             line = line.strip() #remove leading/trailing whitespace
#             #current_line+=f"{line}, "#输出👉name: Introduction to Programming, study credits: 5, （👈此处多了一个逗号）
#             if current_line: #True
#                 current_line+=f"{line}"
#                 combined_line = f"{current_line}, {line}"


#             else: #Since current_line is initially an empty string, the else part is executed. 
#                 current_line = line  # Store the current line for combination
            
#     #result="======================================"
#     #print(result)
# #course_info2(course_info)

def chart_head():
    label_name = 'name'
    exec_nbr = 'exec_nbr'
    exec_pts = 'exec_pts.'
    exm_pts = 'exm_pts.'
    tot_pts = 'tot_pts.'
    grade = 'grade'

    result_1=f"{label_name:<30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade}"
    return result_1

def charts_body():
    names={}
    with open (student_info)as new_file: 
        for line in new_file:
            line = line.replace("\n", "")
            parts=line.split(";")
            if parts[0]=="id":
                continue
            names[parts[0]]=parts[1]+" "+parts[2]

    points={}
    with open (exam_point) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            if parts[0] == "id":
                continue
            point= 0
            # Iterate over the parts list from index 1 to skip the first column
            for n in range(1, len(parts)):
                point+= int(parts[n])
            points[parts[0]]=point

    courses={}
    with open (exercise_data) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            if parts[0] == "id":
                continue
            # Reset course_num for each line
            course_num = 0
            # Iterate over the parts list from index 1 to skip the first column
            for n in range(1, len(parts)):
                course_num += int(parts[n])
            courses[parts[0]]=course_num
            exercise_points = int((((course_num)/40)*100)//10)
    student_info_list = []
    csv_list=[] 
    for id, name in names.items():
        if id in points:
            score = points[id]
            exercise_points = int((((courses[id]) / 40) * 100) // 10)
            overall_point = score + exercise_points
            grade = 0  # Reset grade for each student
            if overall_point <= 14:
                grade = 0
            elif overall_point <= 17:
                grade = 1
            elif overall_point <= 20:
                grade = 2
            elif overall_point <= 23:
                grade = 3
            elif overall_point <= 27:
                grade = 4
            else:
                grade = 5
            
            result_2 = f"{name:<30}{courses[id]:<10}{exercise_points:<10}{score:<10}{overall_point:<10}{grade}"
            result_3=f"{id}; {name}; {grade}"
            csv_list.append(result_3)

            student_info_list.append(result_2)  # Add student information to the list
    return student_info_list

def charts_bod_2():
    names={}
    with open (student_info)as new_file: 
        for line in new_file:
            line = line.replace("\n", "")
            parts=line.split(";")
            if parts[0]=="id":
                continue
            names[parts[0]]=parts[1]+" "+parts[2]

    points={}
    with open (exam_point) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            if parts[0] == "id":
                continue
            point= 0
            # Iterate over the parts list from index 1 to skip the first column
            for n in range(1, len(parts)):
                point+= int(parts[n])
            points[parts[0]]=point

    courses={}
    with open (exercise_data) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            if parts[0] == "id":
                continue
            # Reset course_num for each line
            course_num = 0
            # Iterate over the parts list from index 1 to skip the first column
            for n in range(1, len(parts)):
                course_num += int(parts[n])
            courses[parts[0]]=course_num
            exercise_points = int((((course_num)/40)*100)//10)
    student_info_list = []
    csv_list=[] 
    for id, name in names.items():
        if id in points:
            score = points[id]
            exercise_points = int((((courses[id]) / 40) * 100) // 10)
            overall_point = score + exercise_points
            grade = 0  # Reset grade for each student
            if overall_point <= 14:
                grade = 0
            elif overall_point <= 17:
                grade = 1
            elif overall_point <= 20:
                grade = 2
            elif overall_point <= 23:
                grade = 3
            elif overall_point <= 27:
                grade = 4
            else:
                grade = 5
            
            result_2 = f"{name:<30}{courses[id]:<10}{exercise_points:<10}{score:<10}{overall_point:<10}{grade}"
            result_3=f"{id};{name};{grade}"
            csv_list.append(result_3)
            student_info_list.append(result_2)  # Add student information to the list
    return csv_list

#chart()
def main():
    course_information=course_info2(course_info)
    split_sign=sign()
    charthead=chart_head()
    chartsbody=charts_body()
    chartsbody2=charts_bod_2()

    with open("results.txt", "w") as new_file:
        new_file.write(f"{course_information}\n")
        new_file.write(f"{split_sign}\n")
        new_file.write(f"{charthead}\n")

    with open("results.txt", "a") as new_file:
        for student_info in chartsbody:
            new_file.write(f"{student_info}\n")
    
    with open("results.csv", "w") as my_file:
        for student_info in chartsbody2:
            my_file.write(f"{student_info}\n")
       
main()


