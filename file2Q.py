# f=open('people1-exercise.txt','r')
# c=0
# for i in (f):
#     c+=1
# print(c)
# f.close()



f=open('people1-exercise.txt','r')
data=f.read()
new=data.split("\n")
c=0
i=0
while i<len(new):
    print(new[i])
    c+=1
    i=i+1
print(c)  