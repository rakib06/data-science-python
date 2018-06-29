



### object identity : is
#and 
#or 
#not

if False: #false hole ar khela hbe na

	print('Conditional was True')
else:
	print('vulval')
language='java'

if language=='python':
	print('Conditional was True')
elif language=='java':
	print('java nibe anis sir')
else:
	print("no match")


#and 
#or 
#not
user='Admin'
logged_in=True
if user=='Admin' and logged_in:
	print('asen admin')
else:
	print('Bad ass')
if not logged_in:
	print('plzz Log in')

else:
	print('welcome mia')


a=[1,2,3]
b=[1,2,3]
print(id(a))
print(id(b))
print(a is b)
print(a==b)
a=b
print(a is b )
print(id(a)==id(b))