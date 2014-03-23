#
# Part one
#
print("Part One")
L = list(range(10))
for k in range(10):
    print( L)
    L = L[3:] + L[:3]
print()
#
# Part two 
#
print("Part Two")
K = list(range(10))
for i in range(10):
    print( K)
    dummy = K.pop()
    K = [dummy] + K
print()
#
# Part three
#
print("Part Three")
J = range(10)
for i in range(10):
    print( K)
    dummy = K.pop(0)
    K = K + [dummy]
print()
#
# Part four
#
print("Part Four")
I = range(10)
weight = sum(a ** 2 for a in I)
