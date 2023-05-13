def LineSearch(m,z):
    for i in range(len(m)):
        if m[i] == z:
            return i
    return -1