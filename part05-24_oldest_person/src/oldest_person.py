def oldest_person(people_list: list):#a list of tuples as its argument
    min=people_list[0][1]
    for i in people_list:
        if i[1]<=min:
            min=i[1]
            name=i[0]
    return(name)
if __name__ == "__main__":
    people_list = [('Mary', 1953),('Emily', 2014), ('Arthur', 1977), ('Ernest', 1985),('Ellen', 1997),('Tom', 1923)]
    result = oldest_person(people_list)




    

    



