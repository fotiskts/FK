#1)Γράψτε ένα πρόγραμμα σε Python το οποίο βρίσκει
#τις πέντε μεγαλύτερες λέξεις ενός κειμένου το οποίο
#διαβάζει από αρχείο και τις εκτυπώνει ανάποδα,
#έχοντας αφαιρέσει τα φωνήεντα

def remove_vowel(text):
        for i in "aeiouAEIOU":
            text = text.replace(i,"")
        return text
def rev(x):
  return x[::-1]
            
m=[]
#Δημιουργια αρχειου
f = open("file.txt", "w")
#γραψε στο αρχειο
f.write("Python is an interpreted high level general purpose programming language.")
f.close()#κλεισε το αρχειο
f = open("file.txt", "r")
for line in f:
        line=line.replace('.','')#αφερει τις τελειες
        d = line.split()#χωριζει τις λεξεις του αρχειου
print(d)
f.close()
#Μετραει ποσα γραμματα εχει καθε λεξη
for i in range(len(d)): 
    count=len(d[i]) 
    m.append(count) 
N=len(m)
#ταξινομιση σε αυξουσα σειρα
for j in range(N-1):
    for i in range(N-j-1):
        if m[i]>m[i+1]:
            m[i],m[i+1]= m[i+1],m[i]
            d[i],d[i+1]= d[i+1],d[i]
#κραταει τα 5 τελευταια 
d1 = d[-5:]
newd = ' '.join(map(str, d1))#μετατροπη της λιστας d1 σε string 
D=remove_vowel(newd) #καλει την συναρτηση remove_vowel και αφερει τα φωνηεντα
R=rev(D) #καλει την συναρτηση rev και εκτυπωνει αναποδα τις λεξεις και τα γραμματα
print (R)

