import numpy as np

# ---2 D Array 
student =  np.random.randint(30,100,(2,4))

print(student)

for i in range(2):
    print(student[i])


for i in range(2) :
    for j in range(4) :
        print(student[i][j])


for i,value in enumerate(student,start = 1) :
    print(i,value)

for i in range(2):
    mean = np.mean(student[i])
    print(f"Subject {i+1} Mean: {mean:.2f}")


for i, subject in enumerate(student):
    mean = np.mean(student[i])
    print(f"{subject} Mean: {mean:.2f}")