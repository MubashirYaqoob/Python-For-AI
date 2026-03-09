import numpy as np 

marks = [45, 82, 60, 73, 90, 38, 55, 78]

passed = 0
fail = 0
for i in range(len(marks)) :
    if marks [i] >= 50 :
        passed += 1
    else :
        fail += 1

print(f"passed students {passed},fail students {fail}")

max_marks = np.max(marks)
avg_marks = np.average(marks)

bonus = list(map(lambda x : x + 5 ,marks))

print(bonus)