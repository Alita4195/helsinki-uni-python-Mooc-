limit=int(input("Limit: "))
my_sum=0
sum_string=""
i=1
while my_sum<=limit:
    sum_string+=f"{i}"
    my_sum+=i
    i+=1
    if my_sum<=limit:
        sum_string+="+"

print(f"The consecutive sum:{sum_string}={my_sum}")
    