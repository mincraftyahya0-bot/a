#activity1
empty=[]
print()
num=[1,2,3]
print(num)
tri=[1,2,3]*3
print(tri)
alist=[1,2,3,4,5]
alist=alist[::-1]
print(alist,"\n")
#activity2
def mach(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)

    print("list of words that start and end with the same letter",lst)
    return ctr
count=mach(["abc","cfc","xyz","nyn","1221"])
print(count)
#activity3
l=[4,5,1,2,9,7,10,8]
print("original list:",l)
count=0
for i in l:
    count+=1

avrg=count/len(l)

print("sum =",count)
print("avrage =",avrg)

l.sort()

print("smallest element is",l[0])
print("largest element is",l[-1])
