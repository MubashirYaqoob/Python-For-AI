import numpy as np 
students = np.array([
    # [age, marks, attendance, assignments, passed]
    [20, 75, 90, 8, 1],
    [22, 45, 60, 3, 0],
    [21, 88, 95, 9, 1],
    [19, 55, 70, 5, 1],
    [23, 32, 45, 2, 0],
    [20, 91, 85, 10, 1],
    [22, 61, 75, 6, 1],
    [21, 42, 55, 4, 0],
])
# Columns:
# 0 = age
# 1 = marks
# 2 = attendance
# 3 = assignments
# 4 = passed

marks = students[:,1] # -- marksa agaiye 
print(np.mean(marks))
print(np.argmax(marks))

attend = students[:,2] # -- attendance aagai 

result = students[attend >= 75]

print(result)