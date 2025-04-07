# WATTS / DBM Calculator

import math


def wattgrab():
    watts = int(input("WATTS?> "))
    return watts
    
def wattcalc():  
    watts = wattgrab()
    
    dbm = 10 * math.log10(watts * 1000)
    
    print(dbm)
   


   
def dbmgrab():
    dbm = int(input("DBM?> "))
    return dbm
    
def dbmcalc():
    dbm = dbmgrab()
    
    watts = 10 ** ((dbm - 30) / 10)
    
    print(watts)




def choice():
    
    choose = int(input("""   
[1]WATTS to DBM
[2]DBM to WATTS
    
    """))

    if choose == 1:
        wattcalc()
        
    elif choose == 2:
        dbmcalc()
        
    else:
        print("make a choice")
        choice()
      


choice()
