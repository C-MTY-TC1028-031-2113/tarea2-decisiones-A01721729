import math

def main():
    # Escribe tu código abajo de esta línea
    a =int(input("Da el valor de a: "))
    b =int(input("Da el valor de b: "))
    c =int(input("Da el valor de c: "))

    if a ==0 and b==0:
        print ("No tiene solucion")
    elif a ==0 and b!=0: 
        x = -1 * c/b 
        print(x)
    elif a !=0 and b!=0 :
        discriminante = b**2-4*a*c
        
        if discriminante<0: 
            print("Raices complejas")
        elif discriminante>0:
            x1= (-1*b+math.sqrt(b**2-4*a*c))/(2*a)
            x2= (-1*b-math.sqrt(b**2-4*a*c))/(2*a)
            print(x1)
            print(x2)
        elif discriminante ==0:
            x = -b/(2*a)
            print(x)


if __name__ == '__main__':
    main()
