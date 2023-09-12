'''d = {}
d['name']='shilpa'
d['roll'] = 777
d['marks']=[11,22,33,44]
print(d)
print(d.keys())
print(d.values())
print(d.items())'''

'''
d = {'name':'Shilpa','roll':88,'name':'Anil'}
print(d)
print("KEYS PRINTED")
for keys in d.keys():
    print(keys)
print("VALUES PRINTED")
for val in d.values():
    print(val)
print("KEY, values PRINTED")
for keys,val in d.items():
    print(keys ,"  ---   ", val)
for w in d.items():
    print(w)'''

d = {'name':'Shilpa','roll':88,'marks':77}
print(d.pop('marks'))
print(d)
d.popitem()
print(d)