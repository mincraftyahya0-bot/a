#activity1
mytuple=("tuple",False,3.2,1)
print(mytuple)
mytuple=(1,2,3,4,5)
print(mytuple)
mytuple=mytuple+(6,)
print(mytuple)
tuple1=(1,2,3,4,3,5)
print(tuple1.count(3))
tuple2=(1,2,3,4,5,6,7,8,9,)
slice=tuple2[3:7]
print(slice)
#activity2
def palind(r):
    t=r
    t=t[::-1]
    if t==r:
        print("tuple is flip flop")
    else:
        print("tuple is not flip flop")

palind("12321")
#activity3
weather=(1,0,0,0,1,1,0,1,1)
sun=0
rain=0
for i in range(0,8):
    if i==1:
        sun=+1
    else:
        rain=+1
if sun>rain:
    print("good weather")
else:
    print("bad weather")