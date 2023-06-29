# Write your solution here
import csv

def cheaters():
    with open("start_times.csv") as my_file:
        with open("submissions.csv") as another_file:
            for line1 in csv.reader(my_file, delimiter=";"):
                for line2 in csv.reader(another_file, delimiter=";"):
                    if line2[0]==line1[0]:
                        time=line2[1]-line1[1]
                        print(line2[1],time)

cheaters()