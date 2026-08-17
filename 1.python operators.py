'''python operators'''

a=20
b=10
#1.Arithmetic operators
print("a+b:",a+b) # a+b: 30
print("a-b:",a-b) #a-b: 10
print("a*b:",a*b) # a*b: 200
print("a/b:",a/b)  #a/b: 2.0
print("a//b:",a//b) #a//b: 2
print("a**b:",a**b) # a**b: 10240000000000
print("a%b:",a%b)   #a%b: 0

#2.Comparision operators
print("a<b:",a<b)#a<b: False
print("a>b:",a>b)#a>b: True
print("a>=b:",a>=b)#a>=b: True
print("a<=b:",a<=b)#a<=b: False
print("a==b:",a==b)#a==b: False
print("a!=b:",a!=b)#a!=b: True

#3.Assignment operators
a += 100
print("a+=100:",a)#a+=100: 120
a -= 20
print("a-=20:",a)#a-=20: 100
a *= 10
print("a*=10:",a)#a*=10: 1000
a /= 6
print("a/=6:",a)#a/=6: 166.66666666666666
a //= 5
print("a//=5:",a)#a//=5: 33.0
a %= 2
print("a%=2:",a)#a%=2: 1.0
a **= 2
print("a**=2:",a)#a**=2: 1.0

#4.Logical operators
x = 20
y = 10
print("x%2==0 and y%5 ==0 :",x%2==0 and y%5==0)#x%2==0 and y%5 ==0 : True
print("x%10==0 or y%10 ==0 :",x%10==0 or y%10==0)#x%10==0 or y%10 ==0 : True
print("not x%10==0:",not x%10==0)#not x%10==0: False

#5.Membership operator
s = 'python programming' 
print('x in s:','x' in s) #x in s: False
l = [1,2,3,4]
print('5 not in l:',5 not in l)#5 not in l: True
t = (4,5,6,7)
print('6 not in t:',6 not in t)#6 not in t: False
se = {2,3,3,4,5}
print('3 not in se:',3 not in se)#3 not in se: False
d = {1:1,2:4,3:6,4:16}
print('6 in d:',6 in d)#6 in d: False

#6.idnetity operator
a = [1,2,3,4]
b = [1,2,3,4]
print('a==b:',a==b)#a==b: True
print('a is b:',a is b)#a is b: False
print('a is not b:',a is not b)#a is not b: True
c=a
print('a==c:',a==c)#a==c: True
print('a is c:',a is c)#a is c: True
id(a)
id(b)
id(c)

#7.bitwise operator
print('8 & 3:',8&3)#8 & 3: 0
print('8 | 3:',8|3)#8 | 3: 11
print('8 ^ 3:',8^3)#8<<3: 64
print('~3:',~3)#~3: -4
print('8<<3:',8<<3)#8<<3: 64
print('16>>2:',16>>2)#16>>2: 4

















