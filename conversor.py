import os

import funcoes as fl

loop = 0

def calculo():
    print("========== CONVERSOR DE TEMPERATURA ==========")
    print("1 - Kelvin / Farenheit")
    print("2 - Kelvin / Celsius")
    print("3 - Celsius / Farenheit")
    op = int(input("# "))

    if(op == 1):
        os.system('cls') or None
        print("========== CONVERSOR DE TEMPERATURA ==========")
        print("              Kelvin / Farenheit            ")
        print(" ")
        print("1 - Kelvin -> Farenheit")
        print("2 - Farenheit -> Kelvin")
        resp = int(input("# "))
        if(resp == 1):
            os.system('cls') or None
            tem = int(input("Digite a temperatura: "))
            print(round(fl.kelfer(tem),2))
        
        if(resp == 2):
            os.system('cls') or None
            tem = int(input("Digite a temperatura: "))
            print(round(fl.ferkel(tem),2))


    if(op == 2):
        os.system('cls') or None
        print("========== CONVERSOR DE TEMPERATURA ==========")
        print("              Kelvin / Celsius            ")
        print(" ")
        print("1 - Kelvin -> Celsius")
        print("2 - Celsius -> Kelvin")
        resp = int(input("# "))
        if(resp == 1):
            os.system('cls') or None
            tem = int(input("Digite a temperatura: "))
            print(round(fl.kelcel(tem),2))
        
        if(resp == 2):
            os.system('cls') or None
            tem = int(input("Digite a temperatura: "))
            print(round(fl.celkel(tem),2))

    if(op == 3):
        os.system('cls') or None
        print("========== CONVERSOR DE TEMPERATURA ==========")
        print("              Celsius / Farenheit            ")
        print(" ")
        print("1 - Celsius -> Farenheit")
        print("2 - Farenheit -> Celsius")
        resp = int(input("# "))
        if(resp == 1):
            os.system('cls') or None
            tem = int(input("Digite a temperatura: "))
            print(round(fl.fercel(tem),2))
        
        if(resp == 2):
            os.system('cls') or None
            tem = int(input("Digite a temperatura: "))
            print(round(fl.celfer(tem),2))


while loop == 0:
    calculo()
    print("Você quer consultar novamente?")
    print("1 - Sim      2 - Não")
    tes = int(input("# "))
    if(tes == 1):
        loop = 0

    if(tes == 2):
        break