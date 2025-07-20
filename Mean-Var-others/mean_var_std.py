import numpy as np

def calculate(l):
    # check if number of elements is valid    
    if len(l) < 9:
        raise ValueError("List must contain nine numbers.")
    
    # from list to 3x3 numpy array
    narray = np.array(l)
    narray = narray.reshape((3,3))

    # mean
    mean_r = list(np.mean(narray, axis=0))
    mean_c = list(np.mean(narray, axis=1))
    mean_a = np.mean(narray)

    # variance
    var_r = list(np.var(narray, axis=0))
    var_c = list(np.var(narray, axis=1))
    var_a = np.var(narray)

    # standard deviation
    sd_r = list(np.std(narray, axis=0))
    sd_c = list(np.std(narray, axis=1))
    sd_a = np.std(narray)

    # max 
    max_r = list(np.max(narray, axis=0))
    max_c = list(np.max(narray, axis=1))
    max_a = np.max(narray)

    # min
    min_r = list(np.min(narray, axis=0))
    min_c = list(np.min(narray, axis=1))
    min_a = np.min(narray)
    # sum
    sum_r = list(np.sum(narray, axis=0))
    sum_c = list(np.sum(narray, axis=1))
    sum_a = np.sum(narray)

    calculations = {
        'mean': [mean_r, mean_c, mean_a],
        'variance': [var_r, var_c, var_a],
        'standard deviation': [sd_r, sd_c, sd_a],
        'max' : [max_r, max_c, max_a],
        'min' : [min_r, min_c, min_a],
        'sum' : [sum_r, sum_c, sum_a]
    }

    return calculations