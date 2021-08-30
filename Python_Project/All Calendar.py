import calendar
year = int(input("Enter the Year: "))

#month = int(input("Enter the Month: ")) Eita diye month check korano hoy...

calendar.setfirstweekday(calendar.SATURDAY) #Eita diye Day er serial ta change kora jay...

my_calendar = calendar.calendar(year)
print(my_calendar)





