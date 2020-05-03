exec("""
import time
start_time = time.clock()
w=0
x=0
y=1
limit=0
z=[0,1]
limit=int(input("number: "))
limit=limit-2
print(1)
while w<limit:
    w=y-1
    x=z[y]+z[w]
    z.append(x)
    y=y+1
    print(z[y])
print(time.clock() - start_time, "seconds")
""")