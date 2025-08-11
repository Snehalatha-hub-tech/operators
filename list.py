#creating empty list
"""lst=[]
lst1=list()
print(type(lst))
print(type(lst))"""
#string to list type conversion
S='snehalatha'
l=list(S)#string to list type costing
print(type(S),type(l))
print(l)

##append()
"""l=[1,2,3,5.5,'a','b',1,2,3]
l.append(100)
print("After append operation:",l)"""

##Extend()
"""l=[1,2,3,5.5,'a','b',1,2,3]
l.extend([200,300])
print("After extend operation:",l)"""

# remove(),pop(),clear()del,
"""l=[1,2,3,5.5, 'codegnan','a','b',1,2,3]
print("original list:",l)
l.remove(3)
print("After remove option:",l)
l.pop()
print("After pop operation:",l)
l.pop(3)
print("After pop with position:",l)
del(l[0])
del(l[2:5])
print("After del operation:",l)
l.clear()
print("After clear operation:",l)"""

#min(),max(),sum(),
"""l=[1,2,29,43,3,10,200]
min_val=min(l)
max_val=max(l)
sum_val=sum(l)
print("min value in the list:",min_val)
print("max value in the list:",max_val)
print("sum value in the list:",sum_val)"""

#sort(),reverse()
"""l=[1,2,29,43,3,10,200]
l.reverse()
print("reverse of list:",l)"""

"""#ascending order sort
l=[1,2,29,43,3,10,200]
l.sort()
print(l)
# descending order sort
l=[1,2,29,43,3,10,200]
l.sort(reverse=True)
print(l)"""

##count(value),index(value)
"""count-2==l.count(2)
print("Total 2 elements count:",count-2)
ind=l.index(29)
print("29 value index:",ind)"""

#len(list-name)
l=[1,2,3,10,29,43,200]
length=len(l)
print(length)








