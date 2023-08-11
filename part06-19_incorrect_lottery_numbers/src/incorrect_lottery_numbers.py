# Write your solution here
# def filter_incorrect():

#     with open("lottery_numbers.csv") as new_file:
#         for line in new_file:
#             line=line.strip()
#             new_line=line.split(";") #list without"\n"
#             week_num_split=new_line[0].split(" ")
#             if int(week_num_split[1]):
#                 for item in new_line[1]:
#                     if int(item):
#                         with open("correct_numbers.csv","a")as my_file:
#                             my_file.write(line)
#                     else:
#                         raise ValueError("The week number is incorrect")      
#             else:
#                 raise ValueError("The week number is incorrect")
            
# filter_incorrect()

def filter_incorrect():
    with open("lottery_numbers.csv") as new_file:
        with open("correct_numbers.csv", "w") as my_file:
            for line in new_file:
                line = line.strip()
                new_line = line.split(";") #list without"\n"
                week_num_split = new_line[0].split(" ")
                item_list = []

                if len(week_num_split) == 2 and week_num_split[1].isdigit():
                    for item in new_line[1:]:
                            single_item_list=item.split(",")
                            #print(single_item_list) #list
                            for i in single_item_list:
                                #print(i)
                                if i.isdigit():
                                    if 1 <=int(i) and int(i)<= 39:
                                        if i not in item_list:
                                            item_list.append(i) #fail to remove the repeats
                                            print(item_list)
                                            if len(item_list)!=7:
                                                continue

                                            else:
                                                my_file.write(line+ "\n")                                            
                            #print(item_list)

if __name__ == "__main__":
    filter_incorrect()

    





