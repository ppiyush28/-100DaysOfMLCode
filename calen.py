import calendar
#mnth=int(input('enter the month'))
#year=int(input('enter the year'))
#print (calendar.month(year))

mn=[1,2,3,4,5,6,7,8,9,10,11,12]
yr=2018
#if yr==2018:
for month in mn:
    print (calendar.month(yr,month), '\t')

