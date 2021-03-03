my_dict={'key1':'value1','key2':'value2'}
print(my_dict['key1'])

price_lookup={'apple':80.99,'orange':50.85,'milk':30.50}
print(price_lookup['apple'])

#Complex Dectionries

d={'k1':123,'k2':[0,1,2,3,4],'k3':{'inside k3':100}}
print(d)
print(d['k3']['inside k3'])

print(d['k2'][2])

d2={'k1':['a','b','c']}

print(d2['k1'][2].upper())

d3={'k1':100,'k2':200}
print(d3)
print(d3['k1'])

d3['k3']='Subbu'
print(d3)
d3['k1']='New Value'
print(d3)

