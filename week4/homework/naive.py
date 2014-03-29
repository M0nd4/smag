m = 134456
n = 8121
k = 28411
idum = 1000
ids = set()
for iteration in range(200000):
    idum = (idum * n + k ) % m
    if idum not in ids:
        ids.add(idum)
    else:
        print("We already have idum %d"%idum)
        break;
    
