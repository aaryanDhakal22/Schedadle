from os import listdir
from bs4 import BeautifulSoup
from pprint import pprint

files = listdir("./schedules")
for file in files:
    contents = open("./schedules/" + file, "r").read()
    soup = BeautifulSoup(contents, "html.parser")
    all_rows = soup.find_all("tr")[3:]
    rows_info = []

    for i in all_rows:
        all_info = i.text.split("\n")
        all_info = [i for i in all_info if i != ""]
        print(len(all_info))
        rows_info.append(all_info)

    # pprint(rows_info)
