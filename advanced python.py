#activity1
number1=[1,2,3]
number2=[4,5,6]
result=map(lambda x,y: x+y,number1,number2)
print("number1+number2 :",list(result))
nums=[1,2,3,4,5]
def sq(n):
    return n*n
square=list(map(sq,nums))
print(square)
#activity2
s1=[1,2,3]
s2=["a","b","c"]
s3=list(zip(s1,s2))
print(s3,"\n")

list1=[1,2,3,4]
list2=[100,200,300,400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)

stocks=["reliance","bbc","tcy"]
cost=[2000,1453,3429]
dict_={stocks:cost for stocks,cost in zip(stocks,cost)}
print("\n{}".format(dict_))