num_1 = int(input("Introduce el numero 1: "))
num_2 = int(input("Introduce el numero 2: "))

print("Que operación desea realizar: \n 1: suma \n 2: resta \n 3: multiplicación \n 4: División ")

opc = int(input("Introduce la operacion que quieres realizar: "))


if(opc==1):
    res = num_1+num_2
elif(opc==2):
    res = num_1-num_2
elif(opc==3):
    res = num_1*num_2
elif(opc==4):
    res = num_1/num_2

print("resultado: ",res)
   