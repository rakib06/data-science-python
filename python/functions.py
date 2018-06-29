def helllo_function(grteeting,name='You'):
	#print('helllo_function')
	return '{} Function {}.'.format(grteeting,name)

print(helllo_function('HI',name='Rakib') )


## dictionary 
def student_info(*args,**kwargs): #key word args
	print(args)
	print(kwargs)
student_info('ku','cse' ,subject=['CSE','ECE'], name='john',age=25)
courses=['math','physics']
info={'name':'Rakib','age':23}
student_info(*courses,**info)


######
#number of days per month . first value placeholder for indexing purpose
month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
	return year%4==0 and(year%100!=0 or year%400==0)
def days_in_month(year,month):
	if not 1 <= month <=12:
		return 'invalid month'
	if month==2 and is_leap(year):
		return 29
	return month_days[month]
	

print(is_leap(2020))
print(days_in_month(2016,3))