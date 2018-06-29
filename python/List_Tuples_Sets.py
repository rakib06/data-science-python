
"""
courses_2=['Bangla','English']
courses.insert(0,courses_2 )#oi index a puro list ta add hbe
print(courses[0]) 
courses.remove(courses_2)
courses.extend(courses_2) #2 ta marge hbe 
print('Extend : ')
print(courses)
courses.append('Chemistry') #ENd a ekta element add kora
courses.insert(0,'Art') #prothome ekta element add hbe
print('Before pop')
print(courses)
popped=courses.pop() #FIFO
print('After Pop')
print(courses)
print('pop element')
print(popped)
courses.reverse()
print('After reverse')
print(courses)
courses.sort()
print('After sorting :')
print(courses)
print('descending order :')
courses.sort(reverse=True)
print(min(courses))
print(courses.index('Math'))
print('list comparison')
for item in courses:
	print(item)
"""
courses=['History','Math','Physics','CompSci']
"""
	#loop with index
for index, course in enumerate(courses,start=1):
	print(index,course)
"""

"""
course_str=' -- '.join(courses)
#split
new_list=course_str.split(' - ')
print(course_str)
print(new_list)
"""

"""
####immutable/mutable
list_1=['History','Math','Physics','CompSci']
list_2=list_1
print(list_1)
print(list_2)
##
list_1[0]='Art'
print(list_1)
print(list_2)
##Immutable
tuple_1=('History','Math','Physics','CompSci')
tuple_2=tuple_1
print(tuple_1)
print(tuple_2)

"""
#but not support 
#tuple_1[0]='Art'



 ######SETS 
cs_courses={'History','Math','Physics','CompSci'}
art_courses={'History','Math','Bangla','Art'}
print(cs_courses)
print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(art_courses.difference(cs_courses))
print(art_courses.union(cs_courses))


#Empty list
empty_list=[]
empty_list=list()

#Empty touple
empty_touple=()
empty_touple=tuple()

#Empty Set
empty_set={} # this isn't right ! it's a dictionary
empty_set=set()