student = {
    "ali" : 89,
    "mubashir" : 100,
    "hadi " : 89,
    "hamza" : 80,
    "haris" : 70
}

for marks in student.values() :
    print(marks)  # -- it will return the value of keys


for name ,marks in student.items():
    print(name,marks)