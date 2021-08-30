def main():
    # Escribe tu código abajo de esta línea
    numero = int(input("Introduce los grados: "))
    if(numero<0 or numero> 360):
        print("excede")
    elif(numero==90 or numero ==360 or numero ==270 or numero ==180):
        print("eje")
    elif(0<numero<90):
        print("cuadrante 1")
    elif(90<numero<180):
        print("cuadrante 2")
    elif(180<numero<270):
        print("cuadrante 3")
    elif(270<numero<360):
        print("cuadrante 4")
    

if __name__ == '__main__':
    main()
