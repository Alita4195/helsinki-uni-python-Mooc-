# Write your solution here
def search(persons):
    name = input("name: ")
    if name in persons:
        for value in persons[name]:
            print(value)


    else:
        print("no number")
 
def add(persons):
    name = input("name: ")
    if name in persons:
        addtional_number = input("number: ")
        persons[name].append(addtional_number)

    if name not in persons:
        number = input("number: ")
        persons[name] = [number]
    print("ok!")
 
def main():
    persons = {}
    while True:
        cmd = input("command (1 search, 2 add, 3 quit): ")
        if cmd == "1":
            search(persons)
        if cmd == "2":
            add(persons)
        if cmd == "3":
            break
    print("quitting...")
 
main()