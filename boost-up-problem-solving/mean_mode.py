import numpy as np 
from scipy import stats


arr = [5, 3, 3, 3, 1]

def MeanMode(arr):

    arr = np.array(arr)
    mode = stats.mode(arr)
    mean = np.mean(arr)

    if int(mean) == mode[0][0]:
        return 1
    else:
        return 0

print(MeanMode(arr))
