from os import listdir
from bs4 import BeautifulSoup

files = listdir("./schedules")
for file in files:
    contents = open("./schedules/" + file, "r").read()
    soup = BeautifulSoup(contents, "html.parser")
    print(soup.prettify())
