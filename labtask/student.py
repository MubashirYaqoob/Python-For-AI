class Student:
    def __init__(self, name, id, cgpa):
        self.name = name
        self.id = id
        self.cgpa = cgpa

# Alag naam - class se clash nahi hoga
s1 = Student("Mubashir", 12, 3.5)
s2 = Student("Ali", 21, 3.2)

students = {
    1: s1,
    2: s2
}

# Sahi tarah access karo
print(students[1].name)   # Mubashir
print(students[1].cgpa)   # 3.5
print(students[2].name)   # Ali
