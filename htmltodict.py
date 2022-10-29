from os import listdir
from bs4 import BeautifulSoup
from Schedule import Schedule


def subjects():
    files = listdir("./schedules")
    all_schedules = []
    for file in files:
        contents = open("./schedules/" + file, "r").read()
        soup = BeautifulSoup(contents, "html.parser")
        all_rows = soup.find_all("tr")[2:]
        courses = []

        for i in all_rows:
            all_info = i.text.split("\n")
            all_info = [i for i in all_info if i != ""]
            courses.append(all_info)

        subject = Schedule(courses[0][-1])
        for course in courses:
            subject.add_slots(course[8], course[9], course[1])
            # print(subject)

        all_schedules.append(subject)
    return all_schedules
