from time import sleep
print("Dime algo")
texto = input(str())
print("Procesando mensaje...")
sleep(3)
print("Casi está listo...")
sleep(5)
print("¡Mensaje procesado!")
sleep(2)
print(texto)
sleep(3)
print("¿Ese fue tu mensaje? [Y/N]")
respuesta = input(str())
sleep(1)
if respuesta=="Y" or respuesta=="y" or respuesta=="Yes" or respuesta=="YES" or respuesta=="yes":
    print("Me alegro :)")
elif respuesta=="N" or respuesta=="n" or respuesta=="No" or respuesta=="NO" or respuesta=="no":
    print("Es imposible que me haya equivocado...")
else:
    print("¡ESO NO ES UNA RESPUESTA VÁLIDA! [Y/N]")
    nueva = input(str())
    if nueva=="Y" or nueva=="y" or nueva=="Yes" or nueva=="YES" or nueva=="yes":
        print("Me alegro :)")
    elif nueva=="N" or nueva=="n" or nueva=="No" or nueva=="NO" or nueva=="no":
        print("Es imposible que me haya equivocado...")
    else:
        print("Ya no te dejo más intentos >:(")


#fin--no depurar