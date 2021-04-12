from cuenta_banco import BankAccount

import os

os.system('cls')

cuentas=[]
for i in range(1,3):    
    cuenta = BankAccount()
    cuentas.append(cuenta)    

for cuenta in cuentas:
    os.system("cls")
    
    if cuenta == cuentas[0]:
        for j in range(3):
            deposito = int(input(" cuánto dinero desea depositar cuenta"+str(cuentas.index(cuenta)+1)+": "))
            cuenta.deposit(deposito)
        for k in range(1):
            retiro = int(input(" cuánto dinero desea retirar cuenta"+str(cuentas.index(cuenta)+1)+": "))
            cuenta.withdraw(retiro)
        if (int(cuenta.yield_interest())>0):
            print("Saldo actualizado con la tasa interes es de: $",str(cuenta.yield_interest()))
            press_to_continue=input("presione Enter para contnuar")
            

    if cuenta == cuentas[1]:
        for j in range(2):
            deposito = int(input(" cuánto dinero desea depositar"+str(cuentas.index(cuenta)+1)+": "))
            cuenta.deposit(deposito)
        for k in range(4):
            retiro = int(input(" cuánto dinero desea retirar cuenta"+str(cuentas.index(cuenta)+1)+": "
            ))
            cuenta.withdraw(retiro)
        if (int(cuenta.yield_interest())>0):
            print("Saldo actualizado con la tasa interes es de: $",str(cuenta.yield_interest()))
            press_to_continue=input("presione Enter para contnuar")
    