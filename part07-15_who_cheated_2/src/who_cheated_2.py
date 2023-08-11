
import csv
from datetime import datetime

def final_points():
    submissions = {}
    start_times = {}

    # Read start times from start_times.csv and store them in a dictionary
    with open("start_times.csv") as start_file:
        start_reader = csv.reader(start_file, delimiter=";")
        for line in start_reader:
            start_times[line[0]] = datetime.strptime(line[1], "%H:%M")

    # Read submissions from submissions.csv and update the dictionary with highest points for each task
    with open("submissions.csv") as submissions_file:
        submissions_reader = csv.reader(submissions_file, delimiter=";")
        for line in submissions_reader:
            student = line[0]
            task = int(line[1])
            points = int(line[2])
            submit_time = datetime.strptime(line[3], "%H:%M")
            
            # Ignore submissions made over 3 hours after the start time
            time_difference = submit_time - start_times[student]
            if time_difference.total_seconds() / 3600 > 3:
                continue
            
            if student in submissions:
                if task in submissions[student]:
                    # Update points for the task if higher than the previous submission
                    if points > submissions[student][task]:
                        submissions[student][task] = points
                else:
                    submissions[student][task] = points
            else:
                submissions[student] = {task: points}

    # Calculate total points for each student
    final_points = {}
    for student, tasks in submissions.items():
        total_points = sum(tasks.values())# tasks.values() returns a view object that contains all the values from the tasks dictionary.
        final_points[student] = total_points

    return final_points

if __name__ == "__main__":
    final_points_dict = final_points()
    print(final_points_dict)
