import numpy as np 

marks =  np.random.randint(50,100,(3,5))


for i in range(3) :
    subj_mean = np.mean(marks[i])
    print(subj_mean)


for i in range(3) :  # -- each subject 
    passed = np.sum(marks[i] > 50)
    print(passed)

