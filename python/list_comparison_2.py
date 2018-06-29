friend_list = [
				 ['Soikot', 'Khulna'],
				 ['Hira', 'Satkhira'],
				 ['Rayhan', 'Bagerhat'],
				 ['Rakib', 'Khulna'],
				 ['Asha', 'Khulna'],
				 ['Nisha', 'Khulna'],
				 ['Abir', 'Dhaka']
			]

i=0	
friendlist_str=[' lives in '.join(friend_list[i]) for friend_list[i] in friend_list if friend_list[i][1]!='Khulna']
print(friendlist_str)ans_list_1 = [name + " lives in " + district for name, district in friend_list]
print(ans_list_1)