def add_student(students, name:str): #TOOK TOO MANY DAYS TO SOLVE, NOW STILL HAVE SOME ISSUES BUT CAN BE EXECUTED 
    students[name] = []
 
def add_course(students, name, course):
    test = []
    list_tuple = []
    if course[1]!= 0:  
        students[name].append(course)
        copy=sorted(students[name])[::-1]
        for subject, grade in copy:

            
def print_student(students, name):
    if name in students:
        if students[name]!=[]:
            course_num=len(students[name])
            ave_course_score=0
            print(name + ":", f" {course_num} completed courses:", sep="\n")
            for i in students[name]:      
                ave_course_score+=i[1]/course_num
                print("  "+i[0],i[-1])
            print(f" average grade {ave_course_score}")

        else:
            print(name+":" ," no completed courses", sep="\n")
    else:
        print(name+": no such person in the database")
def summary():
    student_num=0
    for key, value in students.items():
        student_num+=1
    print("students", student_num)

 
if __name__ == "__main__":
    students={}
    add_student(students, "Peter")
    add_student(students, "Eliza") 
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    print_student(students, "Jack")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    summary()






