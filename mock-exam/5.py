import numpy as np 

prices = [100, 250, 180, 320, 90]

dis_price = list(map(lambda x : x % 15 , prices))
filter_price = list(filter(lambda x : x > 200 ,prices ))

total = np.sum(prices)