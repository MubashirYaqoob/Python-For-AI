students = [
    {"name": "Ali",   "grade": "A"},
    {"name": "Sara",  "grade": "B"},
    {"name": "Ahmed", "grade": "A"},
    {"name": "Zara",  "grade": "B"},
    {"name": "Usman", "grade": "A"},
    {"name": "Hina",  "grade": "C"},
]

result = {}
# means A ke ktine B k kitne and so on 
for i in students: # -- yh i jo he vh poori dictionary return kar raha he lekin mujhy sirf gradea chahye 
    grade = i["grade"] # -- i dict ka grade 
    result[grade] = result.get(grade,0) + 1 # -- result dict me grade ka aik keyword bana raha he or us me get ki madad se grade ki value dal raha he or sath me count b kar raha he 

print(result.items())