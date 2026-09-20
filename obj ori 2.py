#activity1
class IOString:
    def __init__(self):
        self.str1=" "
    def get_string(self):
        self.str1=input("Enter the string: ")
    def print_string(self):
        print(self.str1.upper())
str1=IOString()
str1.get_string()
str1.print_string()
#activity2
class employee:
    def __init__(self):
        print("employee created")
    def __del__(self):
        print("employee destroyed")
def create_employee():
    obj=employee()
    print("function end")
    return obj
print("calling create_employee()")
obj=create_employee()
print("program end")
#activity3
class pair_elements:
    def twosum(self,nums,target):
        lookup={ }
        for i,num in enumerate(nums):
            if target-num in lookup:
                return (lookup[target-num],i)
            lookup[num]=i

value=int(input("enter the sum for which you want to make this search: "))
print("index1=%d,index2=%d" % pair_elements().twosum((10,20,30,40,50,60),value))