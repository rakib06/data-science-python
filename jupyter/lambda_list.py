

mylist=[]
for number in range(10):
	if number %2==0:
		mylist.append(number)
print(mylist)

mylist=[number for number in range (10) if number%2==0]
print(mylist)












def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

print(times_tables() == [i*j for i in range(10) for j in range(10) ])
print()



people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) ==(lambda x:x.split()[0] + ' ' + x.split()[-1])(person))


my=lambda person:print(person.split()[0] + ' ' + person.split()[-1])
for person in people:
 	my(person)
 	print(split_title_and_name(person))

print((lambda a, b, c : a + b+c)(1,2,3))
print(list(map(lambda a:a[0]*a[0]+a[-1],[[-1,2],[-2,3],[-3,4]])))
print(list(map(split_title_and_name, people)) )

print(list(map(lambda x  :x.split()[0]+' '+x.split()[-1],people)))
print(list(map(split_title_and_name, people)) == list(map(lambda x  :x.split()[0]+' '+x.split()[-1],people)))


lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
print([b for b in str(range(9,10))])
answer = [a+b+'c'+d for a in lowercase for b in lowercase for c in range(10) for d in digits]

print(len(answer))
answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]
print(len(answer))

import numpy as np
mylist=[[1,2,3],[4,5,6]]
x=np.array(mylist)
print(x)
