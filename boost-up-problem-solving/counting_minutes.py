from datetime import datetime

str1 = '9:00am-10:00am'
str2 = '1:00pm-11:00am'

def CountingMinutesI(str):
    format = '%H:%M %p'
    time1, time2 = list(map(lambda x: datetime.strptime(x[0:x.index('m')-1]+' ' + x[x.index('m')-1:].upper(), format) , str.split("-")))

    print(time1)
    print(time2)
    return (time2-time1, '%M')[0].seconds/60
    

    


print(CountingMinutesI(str1))
print(CountingMinutesI(str2))