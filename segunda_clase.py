#Algunas clases de datos son las siguientes

#String para texto
str
"Hola Mundo"
#Int para numeros 
int 
1,25,0,-15
#floating para numeros decimales
float
2.25, 25.0 
#Listas 
["sal", "agua", "azucar", 1, 2 , 3]
#Diccionarios
{"color ": 'rojo', 'arte':'cine'}
#Tuplas : se escribe siempre entre parentesis y su orden es inmutable
tuple
#(lun',mar', mie',jue', vie')
 #set : es conjunto ordenado de elementos unicos 
set 
 #{a,b,c,d,e}
 #Boleanos : Valores logicos que solo pueden se verdadero o falso
 #bool 
 #True
 #False

 #Variables-----------------------------------------------------------
#Variables tipo texto
pais = "Costa Rica"
pais2 = "Portugal"
print ("Mi pais es " + pais)
print ("Mi pais es :"+ pais + " pero yo vivo en " + pais) 

#Variables tipo numero 
numero1= 55
numero2= 15

print(numero1 + numero2)

#Variables int y float 
num1= 54
num2= 15.2 

print(num1 + num2)

print(type(num2)) #Indica que tipo de variable es 

suma_numeros = num1 + num2
print(suma_numeros)

print(type(suma_numeros)) #Indica que tipo de variable 

#------------------------------------------------------------------------
#Conversion de tipos de datos
#edad = int(input("Dime cual es tu edad: ")) 
#nueva_edad = 1 + edad 
#print("En tu siguiente cumple tendras: " + str(nueva_edad))


#No se puede sumar un string con un int
#edad = input("Dime cual es tu edad: ")
#nueva_edad = edad + 1
#print("En tu siguiente cumple tendras: " + cumple )


#-----------------------------------------------------------------------
#Cadenas
color_auto = "rojo"
matricula = 54123

#FORMAT
print("Mi auto es {} y de matricula {}".format(color_auto, matricula))

#Cadenas Literales
print(f"Mi auto es {color_auto} y de matricula {matricula}")

#x = 10
#y = 5

#print(f"Mis numeros son "+ str(x) + " y " + str(y))
#print("Mis numeros son {} y {}, la suma es :{} ".format(x, y, x+y))

#-----------------------------------------------------------------------
#Operadores Matematicas

x = 6
y = 2
z = 7

print(f"{x} mas {y} es igual a {x+y}")
print(f"{x} menos {y} es igual a {x-y}")
print(f"{x} por {y} es igual a {x*y}")
print(f"{x} dividido {y} es igual a {x/y}")

print(f"{x} elevado a la {y} es igual a {x**y}")
print(f"{x} elevado a la {3} es igual a {x**3}")
print(f"La raiz cuadrada de {x} es igual a {x**0.5}")


#Para averiguar si el numero es par debde salir 0
print(f"{z} modulo de {y} es igual a {z%y}") #osea, impar


#-----------------------------------------------------------------------
#Redondeo
resultado = 90/7
print(resultado)

redondeo = round(resultado)
redondeo = round(resultado,2) #redondeo a 2 digitos
print(redondeo)

valor = 93.666666666
print(round(valor))
print(type(valor))

#-----------------------------------------------------------------------
#Practica
#Trabajas en una empresa donde los trabajadores reciben un comision del
#13% de sus ventas totales. Debes de crear un programa para ayudar a 
#calcular su comision, su nombre y cuanto han vendido ese mes.

nombre = input("Ingrese su nombre: ")
venta_total = int(input("Cual fue el total de sus ventas: "))
comision = round(venta_total*0.13)


print(" Empleado: {} , Total de ventas: {}, Comision: {}".format(nombre, venta_total, comision))