## Transcript Generator
name = input("Enter student name\n")
roll_numb = int(input("Enter your roll number\n"))

print(f"{name} Transcript\n")

# Student dictionary
student = {
    "name": name,
    "roll_number": roll_numb,
    "department": "CS",
    "Semester": 6,
    "courses": {
        "Automata" :{"credit" :3 ,"marks" : 85},
        "AI" :{"credit" :4,"marks" :50},
        "HCI" : {"credit" :3, "marks" :89},
        "SE" :{"credit" :3 ,"marks" : 85},
        "Compiler" :{"credit" :4,"marks" :50},
        "Big_Data" : {"credit" :3, "marks" :89}
    }
}

 # Functio for calculating Grades
def gradeCalculator(marks) :
    if marks >= 90 :
        return 'A+'
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60 :
        return "C"
    else:
        return 'F'
 


# Calculate Semester Gpa 
def gpaCalculator(grade) :
    mapping = {
        "A+" : 4.0,
        "A" : 3.7,
        "B" : 3.0,
        "C" :2.0,
        "F":0.0
    }
    return mapping[grade]

print(f"{'Course':<12} {'Credit':<8} {'Marks':<6} {'Grade':<6}")

total_points = 0
total_credit = 0
for course, info in student["courses"].items():
    credit = info["credit"]
    marks = info["marks"]

    grade = gradeCalculator(marks)
    point = gpaCalculator(grade)
    
    total_points += point * credit
    total_credit += credit
    print(f"{course:<12} {credit:<8} {marks:<6} {grade:<6}")


gpa = total_points / total_credit
print("\nTotal Credit :",total_credit)
print("GPA :",round(gpa,2))


    
    

