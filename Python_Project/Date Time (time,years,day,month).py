import datetime

x = datetime.datetime.now()
print("Now Time = ",x.strftime("%H:%M:%S %p"))
print(x.strftime("Date = %d"))
print(x.strftime("Weekday = %A"))
print(x.strftime("Month = %B"))
print(x.strftime("Year = %Y"))


# R o onek kichu ache janar...

print("Time = ",x.strftime("%H:%M:%S %p"))
print("Full name Year  = ",x.year)
print(x.strftime("Full name Month  = %B"))
print(x.strftime("Full name Day = %A"))
print(x.strftime("Date of Month(01-31) = %d"))
print(x.strftime("Weekday, short version = %a"))
print(x.strftime("Weekday as a number(0-6) = %w"))
print(x.strftime("Month name short = %b"))
print(x.strftime("Month as number = %m"))
print(x.strftime("Short name Year = %y"))
print(x.strftime("Full Year name = %Y"))
print(x.strftime("Time Zone = %Z"))
print(x.strftime("Local Date = %x"))
print(x.strftime("Lacal Date time = %X"))
print(x.strftime("Local date and time = %c"))

# All Varsion Datetime System:
#A reference of all the legal format codes:
'''
Directive:	                                   Description:	                                                       Example:     

%a         ---------                    Weekday, short version                ---------                =   Wed

%A        ---------                     Weekday, full version                  ---------           = Wednesday

%w        ---------           Weekday as a number 0-6, 0 is Sunday      -------           =      3

%d        ---------                     Day of month 01-31                 ---------                       =    31

%b           ---------                  Month name, short version	       ---------                  =   Dec

%B           ---------                  Month name, full version	        ---------             = December

%m        ---------                 Month as a number 01-12        ---------                     =     12

%y        ---------                Year, short version, without century        ---------        = 18

%Y        ---------                    Year, full version           ---------                                =  2018

%H        ---------                     Hour 00-23                      ---------                           =    17

%I        ---------                     Hour 00-12	        ---------                                 =   05

%p        ---------                     AM/PM	        ---------                              =     PM

%M        ---------                     Minute 00-59	        ---------                               =     41

%S        ---------                     Second 00-59	        ---------                                 =   08

%f        ---------                     Microsecond 000000-999999        ---------        =	548513

%z        ---------                     UTC offset        ---------                                      =      +0100

%Z        ---------                     Timezone	        ---------                             =      CST

%j        ---------                     Day number of year 001-366            ---------        =  365

%U   ---------  Week number of year, Sunday as the first day of week, 00-53--------- = 52

%W   --------- Week number of year, Monday as the first day of week, 00-53 --------  = 52

%c        ---------      Local version of date and time        ---------             =  Mon Dec 31 17:41:00 2018	

%x        ---------                     Local version of date	        ---------              =  12/31/18	

%X        ---------                     Local version of time	        ---------              =  17:41:00	

%%        ---------                     A % character	                       ---------                 =    %	

%G        ---------                     ISO 8601 year                          ---------                    =      2018	

%u        ---------                     ISO 8601 weekday (1-7)            ---------                 =   1	

%V           ---------             ISO 8601 weeknumber (01-53)	        ---------              = 01

'''
