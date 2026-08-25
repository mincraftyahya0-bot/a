#activity1
from datetime import date,time,datetime
today=date.today()
now=datetime.now()
print("today is",today)
print("\nnow is",now)
print("\ndate compontnents,",today.year,today.month,today.day)
#activity2
import random
def randdate(start,end):
    print("random date between",start,"and",end)
    randomgen=random.random()
    dformat="%m/%d/%y"

    starttm=time.mktime(time.strptime(start,dformat))
    endtm=time.mktime(time.strptime(end,dformat))

    Randomtm=starttm+randomgen*(endtm-starttm)
    Randomdte=time.strftime(dformat,time.localtime(Randomtm))
    return Randomdte
print(randdate("1/1/2016","12/12/2018"))