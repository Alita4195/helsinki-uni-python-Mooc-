# Write your solution here
import csv
from datetime import datetime

def cheaters():
    cheated_students = []
    with open("start_times.csv") as start_file:
        with open("submissions.csv") as submissions_file:
            start_reader = csv.reader(start_file, delimiter=";")
            submissions_reader = csv.reader(submissions_file, delimiter=";")
            start_reader_data = list(start_reader)
            submissions_data = list(submissions_reader)  # Store submissions data in a list
            
            for line1 in start_reader_data:
                for line2 in submissions_data:
                    if line2[0] == line1[0]:
                        start_time = datetime.strptime(line1[1], "%H:%M")
                        end_time = datetime.strptime(line2[3], "%H:%M")
                        time_difference = end_time - start_time
                        hours = time_difference.total_seconds() / 3600 #.total_seconds()
                        if hours > 3:
                            if line2[0] not in cheated_students:
                                cheated_students.append(line2[0])
            return cheated_students

if __name__ == "__main__":
    cheated_students = cheaters()
    print(cheated_students)
