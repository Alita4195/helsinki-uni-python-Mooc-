import urllib.request
import json

def retrieve_all():
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    my_request = urllib.request.urlopen(url)
    response = my_request.read()
    courses = json.loads(response)
    
    active_courses = []
    item=0
    
        
    for course in courses:
        if course["enabled"]:
            active_courses.append((course["fullName"], course["name"], course["year"], sum(course["exercises"])))

            
    return active_courses



def retrieve_course(course_name: str):
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    my_request = urllib.request.urlopen(url)
    response = my_request.read()
    data = json.loads(response)  # Parse JSON response directly as a dictionary

    weeks = len(data)
    exercises = 0
    students = 0
    hour_total = 0
    
    for week_data in data.values():
        exercises += week_data["exercise_total"]
        students = max(students, week_data["students"])
        hour_total += week_data["hour_total"]
    
    exercises_average = exercises // students
    hours_average = hour_total // students
    
    course_stats = {
        "weeks": weeks,
        "students": students,
        "hours": hour_total,
        "hours_average": hours_average,
        "exercises": exercises,
        "exercises_average": exercises_average
    }
    
    return course_stats
    
if __name__ == "__main__":
    result=retrieve_all()
    print(result)
    course_stats = retrieve_course("docker2019")
    print(course_stats)







