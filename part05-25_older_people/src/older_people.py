# Write your solution here
def older_people(people_list: list, year: int):
    name=[]
    for i in people_list:
        if i[1]<year:
            name.append(i[0])
    return name

if __name__ == "__main__":
    people_list = [('Mary', 1953),('Emily', 2014), ('Arthur', 1977), ('Ernest', 1985),('Ellen', 1997),('Tom', 1923)]
    result = older_people(people_list,1925)
    

    