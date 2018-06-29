nums=[1,2,3,4,5,6,7,8,9,10]
# I want n for each n in nums
my_list=[]
for n in nums:
	my_list.append(n*n)
print(my_list) 
my_list=[n for n in nums[9:0:-2]  ]
print(my_list) 
#bujhini
#using a map + lambda
#map(function,data)
my_list1=list(map(lambda n: n*n , nums))
print('lambda')
print (my_list1)
print('HI')

#Anonymous Function = Lamba Expression 
g=lambda x:3*x+1
print(g(2))
full_name=lambda fn,ln:fn.strip().title()+" "+ln.strip().title()

print(full_name(" rakibul ", "HASAN"))
scifi=["A b","c d"]
help(scifi.sort)
#bujhini
scifi.sort(key=lambda name:name.split(" ")[-1].lower())
print(scifi)

#map example
temps=[("Berlin",29),("Cairo",36),("Rokib",38)]
c_to_f= lambda data:(data[0],data[1]*(9/5)+32)
print(list(map(c_to_f,temps))) #bujlam na


#filter 
import statistics 
data=nums;
avg=statistics.mean(data)
print(avg)
x=filter(lambda x:x<avg,data)
print(list(x))


#Removing missing data 
countries=["","Brazil","Portugal","","Rokib"]
print(list(filter(None,countries)))


#Ruduce 
from functools import reduce 
#Multiply all numbers in a list
data=nums
Multiplier=lambda x,y:x*y
print(reduce(Multiplier,data))
#samething as
product=1
for x in data:
	product=product*x
print(product)
print(1*2*3*4*5*6*7*8*9*10)
print('even')
my_list=[n for n in nums if n%2==0 ]
print(my_list)
print('cross product')
my_list=[(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list) 
print()
#
print('dictionary comprehension')
names=['Rokib','Jebinj','Hadis','Moudud','null']
heros=['CSE','Doctor','Enggr','Businessman','Civil']
print(list(zip(names,heros)))
my_dict={}
for name,hero in zip(names,heros):
	my_dict[name]=hero
print()
print(my_dict)
print()
my_dict={name: hero for name,hero in zip(names,heros) if name!='null'}
print(my_dict)
print()
print('Set comprehension')
nums=[1,1,1,2,3,4,4,6,8,9,4]
my_set=set()
for n in nums:
	my_set.add(n)

print(my_set)
my_set={n for n in nums}

#
print('Generator Expression')
def gen_func(nums):
	for n in nums:
		 yield n*n

my_gen=gen_func({n for n in nums})
for i in my_gen:
	print(i)

print('using list comprehension')

my_gen1=sorted({n*n for n in nums})
for i in my_gen1:
	print (i)