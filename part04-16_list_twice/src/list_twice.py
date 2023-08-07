# Write your solution here
list=[]
while True:
    item=int(input("New item: "))
    if item==0:
        print("Bye!")
        break
    else:   
        list.append(item)
        print(f"The list now: {list}")
        in_order=sorted(list)
        print(f"The list in order: {in_order}")


    
    