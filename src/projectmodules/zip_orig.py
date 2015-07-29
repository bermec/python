#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rog
#
# Created:     27/09/2010
# Copyright:   (c) rog 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass
xx = [1, 1, 3, 7, 5,10, 5, 7]
y = [5, 6, 7, 3, 1, 22, 4, 7]
a = list(zip(xx, y))
b = []
def checktuple(tpl, mylist):
    result = False
    if tpl[::-1] in mylist:
        print("found", tpl[::-1])
        result = True
    return result

for item in a:
    if checktuple(item, a):
        if not item[::-1] in b:
            b.append(item)
if item == a:
    exit()
print("done", b)
print("a = ",a)
exit()







#unzip1, unzip2 = zip(*a)
#unzip1 = zip(*a)i
#print(unzip1)n(a)
f = []
#equiv = d == d
#f = [ (t[0] == t[1]) for t in zip(ix, y) ]
#print(a)
#print(a[0])


#f.append(h)
#for i in range(len(a)):
    #for j in range(len(a)):
        #if  a[i] == a:
            #f.append(a[i])
print(f)
#print(int(sum(f)))
if __name__ == '__main__':
    main()