# Write your solution here
# import json

# def print_persons(filename: str):
#     with open(filename) as my_file:
#         data = my_file.read()
#         people_info = json.loads(data)

#         for person_info in people_info:
#             hobbies = ""
#             for index, item in enumerate(person_info["hobbies"]):
#                 hobbies += item
#                 if index < len(person_info["hobbies"]) - 1:
#                     hobbies += ", "

#             hobbies_set = "(" + hobbies + ")"
#             #print(hobbies_set)

#             print(person_info["name"], person_info["age"], "years", hobbies_set)

# if __name__ == "__main__":
#     print_persons("file1.json")
#以上是我写的代码，以下是标准答案，.join函数是方便了很多。
import json
def print_persons(filename: str):
    with open(filename) as f:
        content = f.read()
    persons = json.loads(content)
    for person in persons:
        name = person['name']
        age = person['age']
        hobbies = ", ".join(person['hobbies'])
        print(f"{name} {age} years ({hobbies})")
if __name__ == "__main__":
    print_persons("file1.json")
