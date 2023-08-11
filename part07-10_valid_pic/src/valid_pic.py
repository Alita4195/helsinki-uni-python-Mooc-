# Write your solution here
#Finnish PICs follow the format ddmmyyXyyyz, where ddmmyy contains the date of birth, 
# X is the marker for century, yyy is the personal identifier and z is a control character.


# def is_it_valid(pic: str):
#     control_num=pic[0:6]+(pic[7:10])#将数字连接到一块
#     index=int(control_num)//31
#     control_character="0123456789ABCDEFHJKLMNPRSTUVWXY"
#     control_character_identifier=control_character[index]




#     if len(pic) != 11:
#         return False
#     else:
#         if pic[0:6].isdigit():
#             if pic[6]=="+" or pic[6]=="-" or pic[6]=="A":
#                 if pic[-1] in control_character:
#                     return True
#     else:
#         return False
from datetime import datetime

# def is_leap_year(year: int):
#     # Check if the year is a leap year
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     return True

def is_it_valid(pic: str):
    # Check the length of the PIC
    if len(pic) != 11:
        return False

    # Define valid markers for centuries
    valid_markers = ['+', '-', 'A']

    # Define the control characters
    control_chars = '0123456789ABCDEFHJKLMNPRSTUVWXY'

    # Extract the components from the PIC
    date_part = pic[:6]
    century_marker = pic[6]
    personal_identifier = pic[7:10]
    control_char = pic[10]

    # Check if the first half of the code is a valid date
    if century_marker == "+":
        prefix_year = "18" + pic[4:6]
    elif century_marker == "-":
        prefix_year = "19" + pic[4:6]
    elif century_marker == "A":
        prefix_year = "20" + pic[4:6]
    else:
        return False

    whole_birth_date = pic[0:4] + prefix_year

    try:
        birth_date = datetime.strptime(whole_birth_date, '%d%m%Y')

        # # Check if the birth date is valid considering leap years
        # if not is_leap_year(birth_date.year) and birth_date.month == 2 and birth_date.day == 29: #When a leap year occurs, an additional day, February 29th, is added to the calendar.
        #     return False

    except ValueError:
        return False

    # Check if the century marker is valid
    if century_marker not in valid_markers:
        return False

    # Calculate the control character
    try:
        nine_digit_number = int(date_part + personal_identifier)
        index = nine_digit_number % 31
        calculated_control_char = control_chars[index]
    except ValueError:
        return False

    # Check if the control character is valid
    if control_char != calculated_control_char:
        return False

    # All criteria are satisfied, PIC is valid
    return True

if __name__ == "__main__":
    print(is_it_valid("230827-906F"))


