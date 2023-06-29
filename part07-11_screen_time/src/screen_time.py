# Write your solution here
# from datetime import datetime, timedelta
# with open ("late_june.txt", "a") as new_file:
    
#     start_date_input = input("Starting date: ")
#     start_date = datetime.strptime(start_date_input, "%d.%m.%Y")

#     days = int(input("How many days: "))
#     end_date=start_date + timedelta(days)
#     new_file.write(f"Time period: {start_date} - {end_date}\n")

#     total_minutes=0
# while days > 0:
#     screen_time = input(f"Screen time ({start_date.strftime('%d.%m.%Y')}): ")
#     another_form_screen_time=screen_time.replace(" ","/")
#     #print(another_form_screen_time)
    
#     #print(screen_time)
#     for item in screen_time:
#         item=screen_time.split(" ")

#     for i in item:
#         total_minutes+=int(i)

#     start_date += timedelta(days=1)
#     days -= 1

# new_file.write(f"Total minutes: {total_minutes}\n")
# average_min=total_minutes/days
# new_file.write(f"Average minutes: {average_min}\n")
# new_file.write(f"{start_date}: {another_form_screen_time}")



# from datetime import datetime, timedelta

# with open("late_june.txt", "w") as new_file:

#     def first_part():
#         start_date_input = input("Starting date: ")
#         start_date = datetime.strptime(start_date_input, "%d.%m.%Y")

#         days = int(input("How many days: "))
#         end_date = start_date + timedelta(days)
#         total_day_num = abs(start_date - end_date).days
#         new_file.write(f"Time period: {start_date.strftime('%d.%m.%Y')} - {end_date.strftime('%d.%m.%Y')}\n")
#         return [start_date, days, total_day_num]

#     def second_part(total_minutes, total_day_num):
#         new_file.write(f"Total minutes: {total_minutes}\n")
#         average_min = total_minutes / total_day_num
#         new_file.write(f"Average minutes: {average_min}\n")

#     def separate_call(result):
#         total_minutes = 0
#         days = result[1]
#         while days > 0:
#             screen_time = input(f"Screen time: {result[0].strftime('%d.%m.%Y')}")
#             another_form_screen_time = screen_time.replace(" ", "/")

#             for item in screen_time.split():
#                 total_minutes += int(item)

#             new_file.write(f"{result[0].strftime('%d.%m.%Y')}: {another_form_screen_time}\n")
#             result[0] += timedelta(days=1)
#             days -= 1
        
#         return total_minutes

#     result = first_part()
#     second_part(total_minutes, result[2])
#     total_minutes = separate_call(result)

# from datetime import datetime, timedelta

# def first_part():
#     start_date_input = input("Starting date: ")
#     start_date = datetime.strptime(start_date_input, "%d.%m.%Y")

#     days = int(input("How many days: "))
#     end_date = start_date + timedelta(days)
#     total_day_num = abs(start_date - end_date).days
#     new_file.write(f"Time period: {start_date.strftime('%d.%m.%Y')}-{end_date.strftime('%d.%m.%Y')}\n")
#     return [start_date, days, total_day_num]

# def separate_call(result, file):
#     total_minutes = 0
#     days = result[1]
#     while days > 0:
#         screen_time = input(f"Screen time {result[0].strftime('%d.%m.%Y')}: ")
#         another_form_screen_time=screen_time.replace(" ","/")

#         for item in screen_time:
#             item=screen_time.split(" ")

#         for i in item:
#             total_minutes+=int(i)

#         file.write(f"{result[0].strftime('%d.%m.%Y')}: {screen_time}\n")
#         result[0] += timedelta(days=1)
#         days -= 1

#     return total_minutes

# def second_part(total_minutes, total_day_num, file):
#     file.write(f"\nTotal minutes: {total_minutes}\n")
#     average_min = total_minutes / total_day_num
#     file.write(f"Average minutes: {average_min}\n")

# with open("late_june.txt", "w") as new_file:
#     result = first_part()
#     total_minutes = separate_call(result, new_file)
#     second_part(total_minutes, result[2], new_file)

from datetime import datetime, timedelta
filename=input("Filename: ")

def first_part():
    start_date_input = input("Starting date: ")
    start_date = datetime.strptime(start_date_input, "%d.%m.%Y")
    print("Please type in screen time in minutes on each day (TV computer mobile): ")
    days = int(input("How many days: "))
    end_date = start_date + timedelta(days)
    total_day_num = abs(start_date - end_date).days
    return [start_date, days, total_day_num]

def separate_call(result, file):
    total_minutes = 0
    days = result[1]
    screen_time_list = []

    while days > 0:
        screen_time = input(f"Screen time {result[0].strftime('%d.%m.%Y')}: ")
        screen_time_list.append(screen_time)
        for item in screen_time.split():
            total_minutes += int(item)
        result[0] += timedelta(days=1)
        days -= 1

    for i, screen_time in enumerate(screen_time_list):
        another_form_screen_time = "/".join(screen_time.split())
        file.write(f"{result[0].strftime('%d.%m.%Y')}: {another_form_screen_time}\n")
        result[0] += timedelta(days=1)

    return total_minutes

def second_part(total_minutes, total_day_num, file):
    file.write(f"\nTotal minutes: {total_minutes}\n")
    average_min = total_minutes / total_day_num
    file.write(f"Average minutes: {average_min}\n")

with open(filename, "w") as new_file:
    result = first_part()
    new_file.write(f"Time period: {result[0].strftime('%d.%m.%Y')}-{(result[0] + timedelta(days=result[1] - 1)).strftime('%d.%m.%Y')}\n")
    total_minutes = separate_call(result, new_file)
    second_part(total_minutes, result[2], new_file)



    











        
    




    
        


