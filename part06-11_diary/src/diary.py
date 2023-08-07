# Write your solution here
print("1 - add an entry, 2 - read entries, 0 - quit")
entry_list=""
while True:
    command=int(input("Function: "))
    
    if command==1:
        
        diary=input("Diary entry: ")
        entry_list+=diary + "\n" #记得加"\n"（new line charater），不然会黏在一起 such as "I ate meatI drank wine"
        with open("diary.txt", "w") as my_file:
            my_file.write(entry_list)
            print("Diary saved")
        
    if command==2:
        with open ("diary.txt") as new_file:
            for line in new_file:
                line = line.replace("\n", "")
                print(line)

    if command==0:
        print("Bye now!")
        break
        


