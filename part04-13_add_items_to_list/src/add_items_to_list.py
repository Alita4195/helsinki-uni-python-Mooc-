# Write your solution here
items=int(input("How many items: "))
item=[]
num=1
while True:
    item.append(int(input(f"Item {num}:")))
    num+=1
    if num>items:
        break
print(item)