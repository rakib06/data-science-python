message="123456789"
messageTwo="""abCDefGhIjABAA"""

""" this is multiline 
comment in python """ 


print(len(message)) #comment
print(message[0:1]) #not index , koto tomo seita
print(message[:6])  # 6 ta porjonto print korbe 
print(message[6:])  # 6th er por theke last porjonto  
print(messageTwo.lower()) # sob lowercase hoye jabe
print(messageTwo.upper()) #sob upper hoye jabe
print(messageTwo.count('a'and 'A')) #koyta 'a' ache count kore dibe
                             # eita case sensitive
# small work , using not case sensitive
messageTheree=messageTwo.lower()
print(messageTheree.count('a'))
#or
print(messageTwo.count('a'.upper()))
##findinf
print(message.find('456')) # surur index dekhabe
print(message.find('10')) #nai tai -1 dekhabe
new_message=message.replace('1234','1111')
print(new_message)
###########

greeting='Hello'
name ='Rokib'

#message = greeting +', '+name +'. Welcome!'
#or
message = '{}, {}. Welcome!'.format(greeting,name)
#or 
message=f'{greeting}, {name.upper()}. Welcome!'
print(message)
#dir function 
print(dir(name))
#string help
#sob jante
print (help(str))
#jekono 1 ta funcction jante 
print(help(str.lower))