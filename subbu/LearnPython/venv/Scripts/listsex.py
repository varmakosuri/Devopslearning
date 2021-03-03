my_list=[1,2,3]
print(my_list)

my_list=['Subbu',100,22.3]
print(my_list)
print("Length", len(my_list))

my_list=['one','two','three']
print(my_list[1:])

another_list=['four','five','six']
total_list=my_list +another_list
total_list[1] ='ALL CAPS TWO'
print(total_list)

#appending- Adding new value to the list
#-------------------#
total_list.append('seven')
print(total_list)

#pop()- it will release the last object in the list
print(total_list.pop())
print(total_list)


#sort() - it will sort your list
alp_list=['x','e','j','k','p']
print(alp_list)
alp_list.sort()
sorted_alplist=alp_list
print(sorted_alplist)

num_list=[100, 10,30,15,20]
print(num_list)
num_list.sort()
sorted_numlist=num_list
print(sorted_numlist)

##reverse() - it will reverse your list

sorted_numlist.reverse();
print(sorted_numlist)
sorted_alplist.reverse()
print(sorted_alplist)
