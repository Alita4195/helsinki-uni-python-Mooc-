# Write your solution here
# import urllib.request
# import json


# my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
# data = my_request.read().decode('utf-8')
# courses = json.loads(data)
# #print(courses)


# def retrieve_all():
#     final_course_list=[]
#     course_list=[]
#     for course in courses:
#         #print(course["enabled"])输出许多行False\True
#         if course["enabled"]=="True":
#             course_list.append(course["fullName"],course["name"], course["year"],course["exercises"])
#             print(course_list)
#             # final_course_list=",".join(course_list)
#             # print(final_course_list)

import urllib.request
import json

def retrieve_all():
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    my_request= urllib.request.urlopen(url)
    
    #type(my_request) #<class 'http.client.HTTPResponse'>
    data=my_request.read()

    courses = json.loads(data)

    active_courses = []
    for course in courses:
        if course["enabled"] == "true":
            active_courses.append(course["fullName"], course["name"], course["year"], sum(course["exercises"]))
    
    print(active_courses)

retrieve_all()





