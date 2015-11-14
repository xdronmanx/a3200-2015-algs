import math

n = raw_input('name: ')

m = math.sqrt(float(n)) 

c = True

a = [False]

for i in xrange(2, int(n)):
    for x in xrange(2,int(m)):
        if i % x == 0 and i != x :
            c = False
    a = a + [c]            
    c = True
print a

