# write your solution here
def matrix_sum():
    with open ("matrix.txt") as new_file:
        sum=0
        for line in new_file:
            line = line.replace("\n", "")
            num_list=line.split(",")
            for items in num_list:
                sum+=int(items)
        return(sum)

def matrix_max():
        with open ("matrix.txt") as new_file:
            largest=0
            for line in new_file:
                line = line.replace("\n", "")
                num_list=line.split(",")
                for items in num_list:
                    if int(items)>largest:
                        largest=int(items)
        return(largest)
def row_sums():
    with open("matrix.txt") as new_file:
        row_sums = []
        for line in new_file:
            line = line.replace("\n", "")
            num_list = line.split(",")
            row_sum = 0
            for item in num_list:
                row_sum += int(item)
            row_sums.append(row_sum)
    return(row_sums)

if __name__=="__main__":
    matrix_sum()
    matrix_max()
    row_sums()
