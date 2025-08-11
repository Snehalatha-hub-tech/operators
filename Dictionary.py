d={1:'a','A':2,6:4,(1,2):4,(1,2):4,5:[1,2,(3,4),5]}
print(d.keys())
#empty dictionary()
d={}
d1=dict()
# dictionary with values
d3={1: 'a', 'A':2, 6:4, (1,2): 4, 5:[1,2,(3,4),5]}
print(d3[1])
print(['A'])
print([5])
#Dictionary methods
d={'language':'python','version': '3.13.5','level':"High level"}
keys=d.keys()
values=d.values()
items=d.items()
print(type(keys))
print(type(values))
print(type(items))
print(keys)
print(values)
print(items)
# dict_items to list type conversion
d={'language':'python','version': '3.13.5','level':"High level"}
items=d.items()
print(type(items))
print(items)
items_list=list(items)
print(type(items_list))
print(items_list)
a,b=items_list[1]
print(a,b)
##pop(key)
d={'language':'python','version': '3.13.5','level':"High level"}
val=d.pop('version')
print(val)
print(d)
## pop  item
d={'language':'python','version': '3.13.5','level':"High level"}
item=d.popitem()
print(item)
print(d)
#accesing and updating  the values
d={'language':'python','version': '3.13.5','level':"High level"}
d['A']=1
d['language']='java'
print(d)
#get(key,default)
d={'language':'python','version': '3.13.5','level':"High level"}
val=d.get('Z',10)
print(val)
#update(dictionary)
d1={'language':'python','version': '3.13.5'}
d2={'language':'java','level':"high level"}
d2.update(d1)
print(d1)
print(d2)
##clear()-remove all items from dictionary
d1={'language':'python','version': '3.13.5'}
d1.clear()
print(d1)
d={'a':[1,2,3,4],3:(40,5,6,7)}
print(d[3][0])




