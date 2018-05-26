import time as t;  # This is required to include time module.

seconds = t.time()
print ("Number of ticks since 12:00am, January 1, 1970:", seconds)

print (t.localtime()) #

localtime = t.localtime(t.time())
print ("Local current time :", localtime)

localtime = t.asctime( t.localtime(t.time()) )
print ("Local current time :", localtime)

import calendar

cal = calendar.month(2016, 2)
print ("Here is the calendar:")
print (cal)


# You can work on timezones
print(t.clock())   # Returns the current CPU time as a floating-point number of seconds. 

t.sleep(30) #30seconds 

x = calendar.isleap(2002)
print(x)


