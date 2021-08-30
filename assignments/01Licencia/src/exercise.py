
def main():
    edad = int(input("Ingresa tu edad: "))

    if(edad<=0):
        print("Respuesta incorrecta")
    elif(edad<18):
        print("No cumples requisitos")
    else:
        ident_Oficial = input("¿Tienes identificación oficial? (s/n): ")

        if(ident_Oficial  != "s" and ident_Oficial  != "n"):
            print("Respuesta incorrecta")

        elif(ident_Oficial  =="n"):
            print("No cumples requisitos")

        elif(edad>=18 and ident_Oficial =="s"):
            print("Trámite de licencia concedido")
            
if __name__ == '__main__':
    main()
