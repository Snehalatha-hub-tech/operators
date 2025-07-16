s="abcde"
print(s[0])
print(s[1])
print(s[-1])
s='abcde'
print(s[1:4])
print(s[2:3])
print(s[ :3])
print(s[ :-2])
print(s[-3: ])
print(s[-4:-1])
print(s[ : :2])
print(s[ : :-1])

s='   abc  '
print(s)
print(s.strip())
print(s.lstrip())
print(s.rstrip())
s= '@@@abc@de@@@'
print(s.strip('@'))
string="I am a python programmer"
print(string.split())

string="I am a student"
print(string.split('a'))

lst=['I', 'am', 'a', 'python', 'programmer']
print(''.join(lst))

string='I am a python programmer'
print(string.find('p'))
print(string.find('z'))

string='I am a python programmer'
print(string.index('p'))
print(string.index('z'))

s1='abcd'
s2='abc123'
s3='1234'
s4='abc@12'
print(s1.isalpha(),s1.isalnum(),s1.isdigit())
print(s2.isalpha(),s1.isalnum(),s2.isdigit())
print(s3.isalpha(),s3.isalnum(),s3.isdigit())
print(s4.isalpha(),s4.isalnum(),s4.isdigit())

s1='abcd'
s2='absd'
print(s1>s2)
print(s1<s2)

s="snehalatha"
print(s.upper().replace('s','@'))                       
print(s.upper().replace('S','@'))

print("_".join("sneha latha".split()))
"""l=list('codegnan')
print(l)"""

print("_".join(list('codegnan')))

#string concationation by using '+'
s1="Code"
s2="Gnan"
print(s1 +  ""  + s2)

s1="welcome"
s2="to"
s3="programming"
print( s1 + "" +  s2  + "" + s3)
#Repetation of string '*'
string="snehalatha"
print(string*3)

string="*"
print(string*1)
print(string*2)
print(string*3)
print(string*4)
print(string*5)

#String case conversion
string="snehalatha"
s2="I am a codegnan student"
print(string.lower())
print(string.upper())
print(string.swapcase())
print(s2.title())
print(s2.capitalize())




      

























































































































































































































































































