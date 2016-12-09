strs=input("Enter the time: ") #HH:MM:SS(AM/PM)
hrs=strs[0:2]
mins=strs[3:5]
secs=strs[6:8]
suffix=strs[8:10]
minutes=int(mins)
seconds=int(secs)
hours=int(hrs)
flag=0
print(hrs,"\t",mins,"\t",secs,"\t",suffix)
if(hours>0 and (minutes<60 and seconds<60)):
    if(suffix=="PM" and hours<12):
        hours+=12
        hrs=str(hours)
    if(suffix=="AM" and hours==12):
            hrs='00'
    if(hours<10):
        hrs='0'+str(hours)
print(hrs,end=':')
print(mins,end=':')
print(secs,end='')
