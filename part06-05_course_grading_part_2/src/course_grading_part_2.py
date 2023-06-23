# wwite your solution here

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_point=input("exam_points1.csv")

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

for id, name in names.items():
    if id in points:
        score = points[id]
        exercise_points = int((((courses[id]) / 40) * 100) // 10)  # Fix: calculate exercise_points for current student
        overall_point = score + exercise_points  # Fix: add exercise_points to score to calculate overall_point
        if overall_point <= 14:
            print(name, 0)
        elif overall_point <= 17:
            print(name, 1)
        elif overall_point <= 20:
            print(name, 2)
        elif overall_point <= 23:
            print(name, 3)
        elif overall_point <= 27:
            print(name, 4)
        else:
            print(name, 5)


