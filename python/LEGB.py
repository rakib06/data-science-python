'''
LEGB
Local, Enclosing ,Global,Built-in
'''
'''
x='gobal x'


def test():
	global x
	x='local x'
	print(x)
test()
print(x)

print()
'''


###
'''
import builtins
print(dir(builtins))


m=min([5,1,4,6,2])
print(m)
def test(z): #z is only local
	
	x='local x'
	print(z)
	#print(x)
test('local z')



'''



def outer():
	x='outer x'
	def inner():
		nonlocal x 
		x='inner x'
		#x='inner x'
		print(x)
	inner()
	print(x)

outer()
