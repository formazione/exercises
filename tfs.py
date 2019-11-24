#%%

from random import randrange
import os


text = """
From our data competitors quality and prices are:

Hotel A, quality 3,  price 4
Hotel B, quality 3,  price 4
Hotel C, quality 3,  price 4
Hotel D, quality 3,  price 4

Our targets are:

Families, quality 3,  price 4
Business, quality 3,  price 4
young, quality 3,  price 4

After you positioned the competitors and the targets,
position your new hotel in this market.
"""

html = ""
for student in range(14):
    html += "<h3>Homework n. " + str(student) + "</h3><br>"
    for line in text.splitlines():
        q = randrange(-5, 5)
        p = q + randrange(-1, 1)
        line = line.replace("quality 3", "quality " + str(q))
        line = line.replace("price 4", "price " + str(p))
        html += line + "<br>"

    html += "<input type='text'>"
    html += "<button>Click me</button>"
    html += "<div style='page-break-before: always'>"

with open("test1.html", "w", encoding="utf-8") as file:
    file.write(html)

os.startfile("test1.html")
