# write your solution here

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

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

names={}
with open (student_info)as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts=line.split(";")
        if parts[0]=="id":
            continue
        names[parts[0]]=parts[1]+" "+parts[2]


for id, name in names.items():
    if id in courses:
        course=courses[id]
        print(name,course)

