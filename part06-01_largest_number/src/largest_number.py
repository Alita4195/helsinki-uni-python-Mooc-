# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        num_1=0
        for line in new_file:
            line = line.replace("\n", "")
            if int(line)>num_1:
                num_1=int(line)
        return(num_1)
if __name__=="__main__":
    largest()

    

