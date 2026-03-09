import numpy as np 

subject = ["Math","Science","English"]
marks = np.random.randint(40,100,(5,3)) # -- 5 rows , 3 cols


for i,row in enumerate(marks,start=1):
    print(f"Student {i}: {dict(zip(subject, row.tolist()))}")
# dict ko bhi f-string ke andar daal do!
    

