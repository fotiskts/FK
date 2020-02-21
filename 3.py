#Γράψτε μια συνάρτηση σε Python η οποία υπολογίζει το ποσό πληρωμής
#όταν της περνάει ο χρήστης τις εγγραφές ενός λεξικού σε λίστα
#για το τι αγόρασε και το ποσοστό φόρου


        
def price(basket):
    for key, value in basket.items():
        if key =="tshirt":
            p=10*value
        elif key =="sweatshirt":
            p=15*value
        else:
            p=20*value 
    s=p+p*0.24
    return s
        
    
    
    

shop={
    "tshirt":10,
    "sweatshirt":15,
    "hoodie":20
    }

print ("""Welcome!!!
choose an option:
0:exit
1:add item
2:view basket
""")


basket={}
option=int(input("option:"))
while option !=0:
    if option==1:
        item=input("enter an item:")
        quantity=int(input("quantity:"))
        basket[item]=quantity
        while item != "tshirt" and item != "sweatshirt" and item != "hoodie":
            print (shop)
            item=input("enter an item from the shop:")
            quantity=int(input("quantity:"))
            basket[item]=quantity
        
    elif option==2:
        for item in basket:
            print (item,':',basket[item])
            
    elif optin!=0:
        print ("Enter a valid option")

    option=int(input("option:"))
print (price(basket))
    

            
