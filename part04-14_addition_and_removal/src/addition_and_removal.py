# Write your solution here
lists=[]
print(f"The list is now {lists}")
while True:
    choice=input("a(d)d, (r)emove or e(x)it:")
    
    if choice=="d":
        if len(lists)==0:
            lists.append(1)
        else:
            lists.append(lists[-1]+1)
            
        print(f"The list is now {lists}")
        
    elif choice=="x":
        print("Bye!")
        break
    elif choice=="r":
        lists.pop(-1)
        print(f"The list is now {lists}")

