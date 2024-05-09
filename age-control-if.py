import datetime

# Determinăm anul curent
current_year = datetime.date.today().year

# Detrminăm vârsta
print("-"*30)
age =current_year - int(input("Anul nașterii ? "))

if age >=0:
    print("Vârsta:",age,"ani")
else:
    print("Eror: Anul nașterii este mai mare decât anul curent !")    

# Detrminăm încadrarea în categoria de vârstă
if age >=0:    
    if age<1 :
       print("Eror: Nu se încadrează în categoriile de vîrstă !")
    elif age<=3 :
        print ("Categoria - baby") 
    elif age<=9 :
        print ("Categoria - kid")
    elif age<=15 :
        print ("Categoria - teen")
    elif age<=18 :
        print ("Categoria - young")         
    elif age<=50 :
        print ("Categoria - adult")         
    else :
        print ("Categoria - old")    

print("-"*30) 