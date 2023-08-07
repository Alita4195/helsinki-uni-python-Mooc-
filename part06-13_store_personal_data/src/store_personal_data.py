# Write your solution here
def store_personal_data(person: tuple):
    with open("people.csv", "a") as file:
        file.write(f"{person[0]};{int(person[1])};{person[2]:.1f}\n")

if __name__ == "__main__":
    person_info = ("Paul Paulson", 37, 175.5)
    store_personal_data(person_info)

# def store_personal_data(person: tuple):
#     with open ("people.csv","a") as file:
#         file.write(f"{person[0]};{int(person[1])};{int(person[2]):1f}\n")

# store_personal_data("Paul Paulson", 37, 175.5)

