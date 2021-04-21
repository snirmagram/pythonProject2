#import datetime
#day=(datetime.datetime.today())
#print(day)
#name of the day
#print(day.strftime("%aA"))
#Monday

#name of the month
#print(day.strftime("%B"))
#april

#name of the year
#print(day.strftime("%Y"))
#2021

#all the the day,year,month and time
#print(day.strftime("%c"))
#Mon Apr 19 14:04:07 2021

#print(type(day.strftime("%c")))

#now = datetime.datetime.today()
#one_day_three_hours = datetime.timedelta(days=1, hours=3)
#print(one_day_three_hours)
#היום
#print(now)
#2021-04-19 14:09:57.036187

#היום של אתמול
#print(now-one_day_three_hours)
#2021-04-18 11:09:57.036187

#היום של מחר
#print(now+one_day_three_hours)
#2021-04-20 17:09:57.036187

#כמה זמן לוקח ללולאה לעשות מיליון סיבובים
#now = datetime.datetime.today()
#for i in range(1000000):
#    pass
#now_2 = datetime.datetime.today()
#print(now_2-now)

#טיימר שסופר כמה זמן יקח לו לשלוח את ההודעה
#import time
#time.sleep(3)
#print("bye")

#מדפיס לוח שנה (לא כולל השנה שאנחנו נמצאים בה עכשיו
#import calendar
#print(calendar.calendar(2020,w=2,l=1,c=3))

import time
#print(time.time())
#print(time.asctime())
print(time.ctime())
