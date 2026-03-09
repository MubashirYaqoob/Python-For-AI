marks = [
    {"name": "Ali",   "marks": 80}, # --student[0]
    {"name": "Sara",  "marks": 95}, # -- student[1]
    {"name": "Ahmed", "marks": 60}, # -- student[2]
    {"name": "Ali",   "marks": 20},  # -- student[3]
]

total = {}

for i in marks:
    name = i["name"]
    score = i["marks"]

    total[name] = total.get(name,0) + score # -- default value return kare ga 

most= max(total)
print(most)

