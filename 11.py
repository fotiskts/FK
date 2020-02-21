#Γράψτε ένα πρόγραμμα σε Python το οποίο έχει μια λίστα από 4άδες αριθμών
#σε ένα αρχείο και παίρνει σαν είσοδο μια 6άδα αριθμών με σειρά προτεραιότητας
#και εμφανίζει το αν υπάρχει διαθέσιμη 4άδα από αυτούς τους 6 αριθμούς

import random

Nfile = open("Numbers.txt", "w")

for i in range(int(input('How many random numbers?:'))):
    line = str(random.randint(1000,9999))
    Nfile.write(line+"\n")
    print(line)
Nfile.close()

n2=[]
number=[]
n =input(":")
n2.append(n)
for item in n2:
    for digit in item:
        number.append(digit)
              

with open('Numbers.txt') as Nfile:
    l = [line.rstrip() for line in Nfile]


count=0
List=[]
for number in l:
    count=0
    for digit in number:
        if digit in n:
            count+=1
    if count==4:
        List.append(number)
        
print ("Οι διαθεσιμες τετραδες ειναι οι παρακατω")
for i in range(len(List)):
               print (List[i])
         
            


            
        
            
            
            
            



        
           
             


