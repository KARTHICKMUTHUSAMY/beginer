year=int(input())
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("yes".format(year))
       else:
           print("no".format(year))
   else:
       print("yes".format(year))
else:
   print("no".format(year))
