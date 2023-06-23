# Write your solution here

def filter_solutions():
    correct_file = open("correct.csv", "w")  # Open correct.csv in write mode
    incorrect_file = open("incorrect.csv", "w")  # Open incorrect.csv in write mode

    with open("solutions.csv") as file:
        for line in file:
            line = line.strip()
            parts = line.split(";")
            name = parts[0]
            calculate = eval(parts[1])
            result = int(parts[2])
            if calculate == result:
                correct_file.write(f"{name};{parts[1]};{parts[2]}\n")  # Write line to correct.csv
            else:
                incorrect_file.write(f"{name};{parts[1]};{parts[2]}\n")  # Write line to incorrect.csv

    correct_file.close()  # Close correct.csv
    incorrect_file.close()  # Close incorrect.csv



if __name__ == "__main__":
    filter_solutions()


#Tiina出现重复2次？
# def filter_solutions():
#     with open("solutions.csv") as file:
#         for line in file:
#             line=line.replace("\n","") #remove两行字之间的空格
#             parts=line.split(";")
#             name=parts[0]
#             calculate=eval(parts[1])
#             result=int(parts[2])
#             if calculate==result:
#                 with open("correct.csv","a") as my_file:
#                     my_file.write(f"{name};{parts[1]};{parts[2]}\n")
#             else:
#                 with open("incorrect.csv","a") as my_another_file:
#                     my_another_file.write(f"{name};{parts[1]};{parts[2]}\n")

# if __name__ == "__main__":
#     filter_solutions()
