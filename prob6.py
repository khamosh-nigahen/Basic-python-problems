import math
C=50
H=30
l=[]
D = raw_input("Please provide the value of D:")
items = [x for x in D.split(",")]
for d in items:
    Q=math.sqrt((2*C*float(d))/H)
    l.append(round(Q))

print l
