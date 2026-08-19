#list types
#a.empty list
print('[]:',[])#[]: []
#b.list with elements
l= [1,2,3,4,5]
print('l:',l)#l: [1, 2, 3, 4, 5]
#c.nested list
s = [[1,2],[3,4],[5,6]]
print('s:',s)#s: [[1, 2], [3, 4], [5, 6]]
#d.list using construtor
sm = list()
print('sm:',sm)#sm: []


#operations on list
l = [1,2,3,4,5,6]
m = [10,20,30,40]
#a.concatination
print('l+m:',l+m)#l+m: [1, 2, 3, 4, 5, 6, 10, 20, 30, 40]
#b.indexing
print('l[2]:',l[2])#l[2]: 3
#c.repetition
print('m*2:',m*2)#m*2: [10, 20, 30, 40, 10, 20, 30, 40]
#d.slicing
print('m[::4]:',m[::4])#m[::4]: [10]
#e.membership
print('100 in m:',100 in m)#100 in m: False


#modifying lists
#a.changing elements
l[2] = 30
print('l:',l)#l: [1, 2, 30, 4, 5, 6]
#b.adding elements
#append
l.append([7,8,9])
print('l:',l)#l: [1, 2, 30, 4, 5, 6, [7, 8, 9]]
#extend
m.extend([70,80,50])
print('m:',m)#m: [10, 20, 30, 40, 70, 80, 50]
#insert
l.insert(2,(3+5j))
print('l:',l)#l: [1, 2, (3+5j), 30, 4, 5, 6, [7, 8, 9]]
#c.removing elements
#remove
l.remove(4)
print('l:',l)#l: [1, 2, (3+5j), 30, 5, 6, [7, 8, 9]]
#pop
l.pop(5)
print('l:',l)#l: [1, 2, (3+5j), 30, 5, [7, 8, 9]]   
#del
del l[2]
print('l:',l)#l: [1, 2, 30, 5, [7, 8, 9]]

#list methods
#clear()
m.clear()
print('m:',m)#m: []
#count(X)
print('l:',l.count(2))#
#sort()
n = [55,76,85,97]
n.sort()
print('n:',n)#n: [55, 76, 85, 97]
#sorted()
print('sorted(n):',sorted(n))#sorted(n): [55, 76, 85, 97]
#reverse()
n.reverse()
print('n:', n)#n: [97, 85, 76, 55]
#max()
print('max(n):',max(n))#max(n): 97
#min()
print('min(n):',min(n))#min(n): 55
#len()
print('len(n):',len(n))#len(n): 4
s = [0,0.0,[],(),{},set(),False]
#any
print('any(s):',any(s))#any(s): False
#all
print('all(s):',all(s))#all(s): False


