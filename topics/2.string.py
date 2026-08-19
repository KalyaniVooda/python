s = "PYTHONISAPROGRAMMINGLANGUAGE"
s1 = "AND PYTHONISEASY"
#1.operations on strings:
#A.concatenation
print('s+' '+s1:',s+' '+s1)#s++s1: PYTHONISAPROGRAMMINGLANGUAGE AND PYTHONISEASY
#B.repetition
print('s*2:',s*2)#s*2: PYTHONISAPROGRAMMINGLANGUAGEPYTHONISAPROGRAMMINGLANGUAGE
#C.indexing
print('s[2]:',s[2])#s[2]: T
#D.slicing
print('s[4:9:1]:',s[4:9:1])#s[4:9:1]: ONISA
print('s[-6:-2:1]:',s[-6:-2:1])#s[-6:-2:1]: NGUA
print('s[2:]:',s[2:])#s[2:]: THONISAPROGRAMMINGLANGUAGE
print('s[:-4]:',s[:-4])#s[:-4]: PYTHONISAPROGRAMMINGLANG
#E.membership
print('O in s:','O' in s)#O in s: True
print('M not in s:','M' not in s)#M not in s: False

#methods in string
#1.Case conversion methods
#A.upper()
print('s.upper:',s.upper())#s.upper: PYTHONISAPROGRAMMINGLANGUAGE
#B.lower()
print('s.lower:',s.lower())#s.lower: pythonisaprogramminglanguage
#C.captalize()
print('s.capitalize:',s.capitalize())#s.capitalize: Pythonisaprogramminglanguage
#D.title()
print('s.title:',s.title())#s.title: Pythonisaprogramminglanguage
#E.swapcase()
print('s.swapcase:',s.swapcase())#pythonisaprogramminglanguage
#F.casefold()
print('s.casefold:',s.casefold())#s.casefold: pythonisaprogramminglanguage


#2.Alignment and Formatting methods
#A.center(width,fillchar)
print("s.center(50,*):",s.center(50,'*'))#s.center(50,*): ***********PYTHONISAPROGRAMMINGLANGUAGE***********
#B.ljust(width,fillchar)
print("s.ljust(50,'*'):",s.ljust(50,'*')) #s.ljust(50,'*'): PYTHONISAPROGRAMMINGLANGUAGE**********************
#C.rjust(width,fillchar)
print("s.rjust(50,'*'):",s.rjust(50,'*')) #s.rjust(50,'*'): **********************PYTHONISAPROGRAMMINGLANGUAGE
#D.Zfill(width)
print("s.zfill(50):",s.zfill(50))#s.zfill(50): 0000000000000000000000PYTHONISAPROGRAMMINGLANGUAGE











