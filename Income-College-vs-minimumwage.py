exec("""
collegeincome=0
year=1
collegetotal=-200000
#worker=22880+24960+27040+29120
worker=0
workersalary=0
while year<=40:
	if year==5:
		collegeincome=50000
	if year>5:
		collegeincome=(collegeincome*1.07)


	collegetotal=collegetotal+collegeincome
	if year<6:
		workersalary=2080*(11+(1*(year-1)))
		worker=worker+workersalary
	if year>5:
		workersalary=2080*15
		worker=worker+workersalary

	if collegetotal>worker:
		print("Year: ",year)
		print("SUCCESS")
		print("College Yearly Salary: ",collegeincome)
		print("College Net Worth: ",collegetotal)
		print("Worker Net Worth: ",worker)
		print("Worker Salary: ",workersalary)
	else:
		print("Year: ",year)
		print("College Yearly Salary: ",collegeincome)
		print("College Net Worth: ",collegetotal)
		print("Worker Net Worth: ",worker)
		print("Worker Salary: ",workersalary)
	year=year+1
""")