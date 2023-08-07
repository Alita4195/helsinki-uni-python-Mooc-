# Write your solution here

# from datetime import datetime, timedelta


# filename = input("Filename: ")


# def first_part():
#     start_date_input = input("Starting date: ")
#     start_date = datetime.strptime(start_date_input, "%d.%m.%Y")
    
#     days = int(input("How many days: "))
#     print("Please type in screen time in minutes on each day (TV computer mobile): ")
#     end_date = start_date + timedelta(days - 1)
#     # total_day_num = abs(start_date - end_date).days
#     # print("After first_part(): ",[start_date, days, end_date])
#     return [start_date, days, end_date] # function returns a list


# def separate_call(result, file):
#     total_minutes = 0
#     days=result[1]
#     screen_time_list = []
#     param1 = result #param1[0] does change
#     screen_time_enu = []

#     while days > 0:
#         screen_time = input(f"Screen time {param1[0].strftime('%d.%m.%Y')}: ") #输出格式不满足题目要求
        
#         for item in screen_time.split(" "):
#             total_minutes += int(item)
#             screen_time_list.append(item)
#             #print(screen_time_list) 最终输出["10","10", "10"] okay
#             another_form_screen_time = "/".join(screen_time_list)
#             #print(another_form_screen_time) 最终输出[10/10/10] okay
            
#             file.write(f"{param1[0].strftime('%d.%m.%Y')}: {another_form_screen_time}\n")

#         #print((result[0].strftime('%d.%m.%Y')),": ", screen_time_list) #输出24.06.2020 :  ['10 10 10']



#         days -= 1
#         param1[0] += timedelta(days=1)

        
    
#     # for screen_time in screen_time_list:
#         # another_form_screen_time is like "10/10/10"
        

#         #screen_time_enu.append()

#     return total_minutes, another_form_screen_time# returns a tuple


# def second_part(total_minutes, result, file):
#     file.write(f"\nTotal minutes: {total_minutes}\n")
#     average_min = total_minutes / int(result[1])
#     file.write(f"Average minutes: {average_min}\n")


# with open(filename, "w") as new_file:
#     result = first_part()

#     new_file.write(
#         f"Time period: {result[0].strftime('%d.%m.%Y')}-{(result[2]).strftime('%d.%m.%Y')}"
#     )
#     total_minutes, another_form_screen_time= separate_call(result, new_file)

#     second_part(total_minutes, result, new_file)
from datetime import datetime, timedelta

filename = input("Filename: ")


def first_part():
    start_date_input = input("Starting date: ")
    start_date = datetime.strptime(start_date_input, "%d.%m.%Y")
    
    days = int(input("How many days: "))
    print("Please type in screen time in minutes on each day (TV computer mobile): ")
    end_date = start_date + timedelta(days - 1)
    
    return [start_date, days, end_date]  # function returns a list


def separate_call(result, file):
    total_minutes = 0
    days = result[1]
    screen_time_list = []
    current_date = result[0]  # Track the current date separately
    line=""
    
    while days > 0:
        screen_time = input(f"Screen time {current_date.strftime('%d.%m.%Y')}: ")
        
        for item in screen_time.split(" "):
            total_minutes += int(item)
            screen_time_list.append(item)
            another_form_screen_time = "/".join(screen_time_list)
        line+=(f"{current_date.strftime('%d.%m.%Y')}: {another_form_screen_time}\n") #输出12.02.2023: 10/10/10，13.02.2023: 10/10/10/10/10/10
        print(line) 
        
        days -= 1
        current_date += timedelta(days=1)  # Update the current date
    
    

    return total_minutes, line  # returns a tuple


def second_part(total_minutes, result, file):
    file.write(f"\nTotal minutes: {total_minutes}\n")
    average_min = total_minutes / int(result[1])
    file.write(f"Average minutes: {average_min}\n")


with open(filename, "w") as new_file:
    result = first_part()

    new_file.write(
        f"Time period: {result[0].strftime('%d.%m.%Y')}-{result[2].strftime('%d.%m.%Y')}\n"
    )
    total_minutes, line = separate_call(result, new_file)
    
    second_part(total_minutes, result, new_file)
    



    


