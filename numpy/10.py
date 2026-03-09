import numpy as np

scores = np.array([
    # [student_id, math, english, science]
    [1, 85, 70, 90],
    [2, 45, 80, 60],
    [3, 92, 55, 88],
    [4, 38, 65, 72],
    [5, 78, 90, 85],
])

math = scores[:,1] 
print(np.mean(math))