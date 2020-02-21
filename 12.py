#Γράψτε ένα πρόγραμμα σε Python το οποίο παίρνει μια ημερομηνία σε
#μορφή ΗΗ/ΜΜ/ΕΕΕΕ και εμφανίζει πόσες μέρες/ώρες/δευτερόλεπτα απέχει
#αυτή από σήμερα καθώς και πόσες ημέρες έχει ο μήνας εκείνης της ημερομηνίας

import datetime
from datetime import date
isValid=False
while not isValid:
    Date = input("Enter the Date (dd/mm/yyyy) : ")
    try:
        d = datetime.datetime.strptime(Date, "%d/%m/%Y")
        isValid=True
    except:
        print ("enter the date in dd/mm/yyyy format \n")
day,month,year = Date.split('/')
year=int(year)
month=int(month)
day=int(day)
Date=date(year,month,day)
today=date.today()
D=Date-today
H=D.days*24
S=H*3600
if month==1 or month==3 or month==5 or month==7 or month==8 or month==12:
    days=31
elif month==4 or month==6 or month==9 or month==11:
    days=30
elif month==2:
    if (year%4)==0 and (year%100)!=0 or (year%400)==0:
        days=29
    
    else:
        days=28

print ("Η ημερομηνια απεχει",D.days,"μερες\n",H,"ωρες\n",S,"δευτερολεπτα\n και ο μήνας εκείνης της ημερομηνίας εχει",days,"ημερες")

