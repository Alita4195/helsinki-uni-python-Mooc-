# Write your solution here
def new_person(name:str, age: int):
    new_person=()
    if name=="":
        raise ValueError("name is an empty string")
    if len(name)>40:
        raise ValueError("name is longer than 40 characters")
    if " " not in name:
        raise ValueError("name contains less than two words")
    if age<0:
        raise ValueError("age is a negative number")
    if age>150:
        raise ValueError("age is greater than 150")
    else:
        new_person+=(name, age)
        return new_person


if __name__ == "__main__":
    while True:
        name=str(input("Your name: "))
        age=int(input("Your age: "))

        new_person(name, age)


