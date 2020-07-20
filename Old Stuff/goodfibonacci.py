exec("""
import time
start_time = time.clock()
total=0
last=0
current=1
temp=0
count=0
limit=int(input("number: "))
limit=limit-1
print(1)
while count<limit:
	temp=current
	current=current+last
	last=temp
	count=count+1
	print(current)
print(time.clock() - start_time, "seconds")
""")
