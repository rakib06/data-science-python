student={'name':'john','age':25,'courses':['Math','ComputerScience']}
print(student['name']) #osthir
print(student['courses'])
print(student.get('courses','Not Found'))
student['name']='Rakib'
student['phone']='01950-641081'
print(student.get('phone','Not Found'))
print(student['name']) 
student.update({'name':'Hasan','cgpa':'3.10'})
print(student)
del student['age']
print(student)
student['age']=25
age=student.pop('age')
print(age)
print(len(student)) #number of keys
print(student.keys()) #name of keys
print(student.values()) 
print(student.items()) #all
for key,value in student.items():
	print(key,value)
key=[(key,value) for key,value in student.items() ]
print(key)