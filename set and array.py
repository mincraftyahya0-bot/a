#activity1
my_set={1,2,3}
print("my set :",my_set)
my_set={1,"hi",(1,2,3)}
print("my set now :",my_set)
my_set={1,2,3,3,4,5,3,4}
print("my set now :",my_set)
my_set=set([1,2,3,2])
print("my set now :",my_set)
my_set=set([1,2,3,4,5])
print("original set :",my_set)
my_set.pop()
print("my set now :",my_set)
#activity2
setx={"yellow","blue"}
sety={"blue","green"}
print(setx,sety)
setz=setx.intersection(sety)
print(setz)
#activity3
import array as arr
count=0
_array=arr.array("i",[1,2,3,3,4,5,3,6,3])
print(_array)
for i in _array:
    if i == 3:
        count+=1
print(count)