rate_USD_to_ERO = 0.93
rate_ERO_to_MDL = 19.09
rate_USD_to_MDL = 17.74
print("-"*30)
print ("1 = USD/EURO\n2 = EURO/USD\n3 = MDL/EURO\n4 = EURO/MDL\n5 = MDL/USD\n6 = USD/MDL")
input_currency = int(input("Indică varianta de convertire: "))

if 0 < input_currency <= 6:
    input_amount = float(input("Indică cantitatea: " )) 
    if input_currency == 1:
        mony = input_amount*rate_USD_to_ERO
        print ("Veți primi:",round(mony,2),"EURO" )
    elif input_currency == 2:
        mony = input_amount/rate_USD_to_ERO 
        print ("Veți primi:",round(mony,2),"USD" )
    elif input_currency == 3:
        mony = input_amount/rate_ERO_to_MDL
        print ("Veți primi:",round(mony,2),"EURO" )
    elif input_currency == 4:
        mony = input_amount*rate_ERO_to_MDL
        print ("Veți primi:",round(mony,2),"MDL" )
    elif input_currency == 5:
        mony = input_amount/rate_USD_to_MDL
        print ("Veți primi:",round(mony,2),"USD" )
    elif input_currency == 6:
        mony = input_amount*rate_USD_to_MDL
        print ("Veți primi:",round(mony,2),"MDL" )
else:
    print ("error: Indicați una din cele 6 variante !" )

print("-"*30)


