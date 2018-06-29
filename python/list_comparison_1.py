friend_list = [
				 ['Soikot', 'Khulna'],
				 ['Hira', 'Satkhira'],
				 ['Rayhan', 'Bagerhat'],
				 ['Rakib', 'Khulna'],
				 ['Asha', 'Khulna'],
				 ['Nisha', 'Khulna'],
				 ['Abir', 'Dhaka']
			]


for i in range(len(friend_list)):
	friendlist_str=' lives in '.join(friend_list[i])
	print(friendlist_str)
v=[2,-3,1]
i=0
v4=[4*x for x in v ]
print(v4)

ans=[name + " lives in " + district for name,district in friend_list[-8:-3]  if district!='Khulna']
print(ans)
A=[1,3,5]
B=[2,3,4]
ab=[(num , word)  for num in A for word in B]# in A and word in B ]
print(ab)
my_list=[0,1,2,3,4,5,6,7,8,9]



print(my_list[-1:2:-4])#suru:sesh er age : koto kore kombe
print(my_list[::-1])#purotai ultay jabe)
url='http://rokib.com'
print(url[-3:16:1])
print(url[7:-4:]) #kontar pore ar kontar age suru hbe  
