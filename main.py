from htmltodict import subjects
from pprint import pprint

subs = subjects()
perms = []
for i in subs[0].slots:
    for j in subs[1].slots:
        for k in subs[2].slots:
            if not (
                i.collide_time(j) or j.collide_time(k) or k.collide_time(i)
            ):
                perms.append([i, j, k])

for i in perms:
    print(i)
