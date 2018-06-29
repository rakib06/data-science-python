li=[9,-1,-8,6,5,3,7]

s_li=sorted(li,key=abs)

print('abs sorted variable :\t',s_li)
li.sort()
print('original variable :\t',li)
s_li1=li.sort()
print('mistake:\t',s_li1)
s_li=sorted(li,reverse=True)
print('Reverse sorted variable :\t',s_li)
tup=(9,1,8,6,5,3,7)
s_tup=sorted(tup)
#tup.sort()
#print('Tuple\t',tup) hbe na
print('Tuple\t',s_tup)

#for dictionary 
di={'name':'Corey','job':'programming','age':None,'os':'windows'}
s_di=sorted(di,reverse=True)
print('Dictionary\t',s_di)



#Example
class Employee:
	def __init__(self,x,y,z):
		self.name=x
		self.age=y
		self.salary=z

	def __repr__(self):#representation
		return'({},{},${})'.format(self.name,self.age,self.salary)
e1=Employee('Rokib',31,70000)
e2=Employee('Sarah',36,8000)
e3=Employee('Tamim',32,900000)

employees=[e1,e2,e3]
'''
employees=[
	Employee('Rokib',32,70000),
	Employee('Sokib',32,70000),
	Employee('Pokib',32,70000)	
]
'''
print()
print('object sorting salary')
def e_sort(emp):
	return emp.salary #emp.salary

s_employees=sorted(employees,key=e_sort,reverse=True) #key=lambda e: e.name

print(s_employees)

print('using lambda name')
s_employees=sorted(employees,key=lambda e: e.name,reverse=False)
print(s_employees)
print('using oparator age')
from operator import attrgetter
s_employees=sorted(employees,key=attrgetter('age'))
print(s_employees)

	