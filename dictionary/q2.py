import numpy as np 
sessions = np.array([
    [6, 82, 3, 45, 1],   # Session 1
    [1, 36, 7, 40, 1],   # Session 2
    [8, 91, 2, 14, 0],   # Session 3
    [4, 70, 4, 32, 1],   # Session 4
    [3, 55, 5, 28, 1],   # Session 5
    [7, 88, 2, 55, 1],   # Session 6
    [2, 42, 8, 15, 0],   # Session 7
    [5, 78, 3, 40, 1],   # Session 8
    [1, 30, 9, 8,  0],   # Session 9
])

# -- get one column 
sessions[:,0] # -- column 1 : sari rows , 0 pehla column
sessions[:,1] # -- column 1 


np.mean(sessions[:,1]) # -- quiz column ka mean nikal liya 
def productivity_score(sessions):
    hours     = sessions[:, 0]  # col ?
    cups      = sessions[:, 2]  # col ?
    submitted = sessions[:, 4]  # col ?

    score = (hours * 2) + (submitted * 1.5) - (cups * 0.5)

    return score

print(productivity_score(sessions))