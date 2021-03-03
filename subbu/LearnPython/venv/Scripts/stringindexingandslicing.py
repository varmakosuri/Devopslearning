mystring="Hello World"
print(mystring[1])

mystring2='abcdefghijk'
print(mystring2[:3])
print(mystring2[1:3])
print(mystring2[::])
print(mystring2[::3])
#strings are immutable objects means we can't change the content of the objects
print(mystring.split())
#Print Formatting with Strings
#------------------------------------#
my_name='Subbu'
print("Hello" +my_name)
print('this is a string {}'.format('INSERTERD'))
print('The {2} {1} {0}'.format('fox','brown','quick'))

print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

#Float Formating
result=100/777
print("The result was {r:1.3f}".format(r=result))