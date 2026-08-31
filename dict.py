#activity1
student_data={"id1":{"name":"alex","class":"V","age":9},"id2":{"name":"jack","class":"V","age":7},"id3":{"name":"alex","class":"V","age":9},"id4":{"name":"mohamad","class":"V","age":10}}

result={}
seen=[]

for student_id,details in student_data.items():
    special_key={details["name"],details["class"],details["age"]}

    if special_key not in seen:
        seen.append(special_key)
        result[student_id]=details


for k,v in result.items():
    print(k,":",v)
#activity2
testdic={"a":2,"b":2,"c":2,"d":3}
print("original dic:",str(testdic))
k=2
res=0
for key in testdic:
    if testdic[key]==2:
        res=res+1
print("frequency of k:",res)
#activity3
concode={"india":91,"astralia":25,"nepal":977}
print("contry code of india:",concode.get("india","-not found"))
print("contry code of japan:",concode.get("japan","-not found"))