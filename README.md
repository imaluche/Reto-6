# Reto-6 Funciones 1

Ejercicio 1:
------------------
```python
    import math
    numeropi= math.pi
    radio_esf:float
    radio_con:float
    altura:float
    def volumen_figura(radio_esf,radio_con,altura):
    volumen_esf:float= (4/3)*(radio_esf**3)*numeropi
    volumen_con:float= (numeropi*(radio_con**2)*altura)/3
    volumen_total:float= volumen_esf+volumen_con
    return volumen_total
    def area_figura(radio_esf,radio_con,altura):
    area_esf:float=4*numeropi*(radio_esf**2)
    area_con:float= numeropi*(radio_con**2)+(numeropi*radio_con*altura)
    area_total:float=area_con+area_esf
    return area_total
    if __name__=="__main__":
    radioe=float(input("ingrese radio de la esfera en centimetros"))
    radioc=float(input("ingrese radio del cono en centimetros"))
    alt=float(input("ingrese altura del cono en centimetros"))
    volfinal=volumen_figura(radioe,radioc,alt)
    areafinal=area_figura(radioe,radioc,alt)
    print("el volumen de la figura es " + str(volfinal) + " centimetros cubicos")
    print("el radio final es"+ str(areafinal)+ " centimetros cuadrados")
```
## Explicacion:
+ Para poder realizar con fidelidad las ecuaciones de circunferencias es necesario importar el numero pi, este se puede traer
desde el paquete math para usarlo como una variable a parte
+ Hecho esto creamos 2 funciones que contengan dentro las formulas de volumen y area del cono y esfera respectivamente para al final de la
funcion sumar sus valorer
+ Esta suma de areas/volumenes seran lo que nos devolvera la funcion al invocarla
+ Añadimos a nuestro codigo variables introducibles por teclado que representen los valores radios y altruras de las figuras
+ Aplicamos las funciones con estas variables ingresadas y creamos un print que nos de el resultado en valores entendibles

Ejercicio 2:
------------
```python
     import math
Pi=math.pi
a:float
b:float
radio:float
def area (a,b,radio):
    area_rectangulo:float=a*b
    area_rueda= Pi*(radio**2)
    area_total=area_rectangulo+ (2*area_rueda)
    return area_total
def perimetro (a,b,radio):
    per_rectangulo:float=(2*(a+b))
    per_rueda:float=2*Pi*radio
    per_total:float=per_rectangulo+(2*per_rueda)
    return per_total
if __name__=="__main__":
    ladoa:float=float(input("valor del primer lado del rectangulo en centimetros"))
    ladob:float=float(input("valor del segundo lado del rectangulo en centimetros"))
    radio:float=float(input("valor del radio de las ruedas en centimetros"))
    areafinal= area(ladoa,ladob,radio)
    perfinal=perimetro(ladoa,ladob,radio)
    print("el area del carro es "+str(areafinal)+ " centimetros")
    print("el perimetro del carro es "+str(perfinal)+ " centimetros")
```
## Explicacion
+ Similar al ejercicio 1 importamos el numero Pi para las circunferencias, pero esta vez solo se usaran en las "ruedas"
+ Dentro de la primera funcion definimos las ecuaciones de area del circulo y del rectangulo para despues sumarlas en un
area total (el valor del circulo se multiplica por 2 pues hay 2 circulos de igual radio), este valor total sera el devuelto
por la funcion
+ En la segunda funcion definimos el perimetro del circulo y el rectangulo para despues formar el perimetro total siguiendo
los mismos lineamientos que en el area, hecho esto el perimetro total sera lo que nos devolvera la funcion
+ Repetimos el proceso posterior a la funciones hecho en el ejercicio 1, creando valores ingresados por teclado e invocando a
las funciones para usar estos valores para al final usar un print que nos de el resultado en valores entendibles

Ejercicio 3:
-----------
```python
     g:float
G:float
p:float
def carnedeaves(g,G,p):
    kg_gallinas=6*g
    Kg_gallos=7*G
    kg_pollos=1*p
    Kg_total=kg_gallinas+kg_pollos+Kg_gallos
    return Kg_total
if __name__=="__main__":
    gallinas:float=float(input("¿cuantas gallinas tienes?"))
    gallos:float=float(input("¿Cuantos gallos tienes?"))
    pollos:float=float(input("¿Cuantos pollos tienes?"))
    masa=carnedeaves(gallinas,gallos,pollos)
    print("en total tus aves suman un peso de "+ str(masa)+" kilogramos")
```
## Explicacion
+ Definimos una funcion en la cual representemos el valor de peso de cada animal multiplicado por el numero que se tiene
+ En esta misma funcion se suman estos valores de pesos para obtener el peso total
+ Hecha la funcion incluimos en el codigo variables que se puedan asginar por teclado, una para cada ave
+ Aplicamos estas variables en la funcion para usarlas en un print que nos de el numero en unidades comprensibles

Ejercicio 4:
-----------
```python
     def precio(p:float,l:float,h:float,t:float):
    precio_p=p*300
    precio_l=l*3300
    precio_h=h*350
    preciot=precio_p+precio_l+precio_h
    cuantofalta= t-preciot
    return cuantofalta
if __name__=="__main__":
    npanes:float=float(input("numero de panes que te pidieron"))
    nleche:float=float(input("numero de bolsas de leche que te pidieron"))
    nhuevos:float=float(input("numero de huevos que te pidieron"))
    dinero:float=float(input("cuanto te dio tu mamá"))
    vueltas=precio(npanes,nleche,nhuevos,dinero)
    print("tus vueltas son "+str(vueltas)+ " pesos")
```
## Explicacion
+ Al igual que en el ejercicio 3 definimos el valor en precio del producto tomando en cuenta el numero pedido
+ Definimos un precio total como la suma de los precios individuales de cada producto
+ definimos otra variable que nos muestre la diferencia entre el dinero que se nos dio y el precio total
+ En el codigo principal añadimos variables asignables por teclado para cada uno de los productos y el dinero
que se nos fue entregado para las compras
+ aplicamos la funcion con las variables introducidas
+ Escribimos un print que nos de las vueltas en pesos
  
Ejercicio 5:
-----------
```python
     def interes(p:float,po:float,t:float):
    valorpor= (po)/100
    costo= p(valorpor+1)**t
    return costo
if __name__=="__main__":
    prestamo:float=float(input("valor del prestamos en pesos"))
    porcentaje:float=float(input("interes mensual representado en porcentaje"))
    tiempo:float=float(input("duracion del prestamo en meses"))
    valorprestamo=interes(prestamo,porcentaje,tiempo)
    print("el valor que se tendra que pagar despues de "+str(tiempo)+" meses es "+str(valorprestamo)+" pesos")
```
## Explicacion:
+ Definimos una funcion en la que apliquemos la formula de interes compuesto tomando en cuenta el dinero prestado en
pesos , el interes impuesto en porcentaje y la duracion del prestamo en meses
+ La funcion retornara el resultado del interes compuesto
+ dentro del codigo principal definimos 3 valores introducibles mediante teclado para las 3 variables que debe tomar la
funcion
+ Aplicamos la funcion con las variables introducidas
+ En un print representamos el resultado con valores y descripciones comprensibles


Ejercicio 6:
-----------
```python
     def contagios(co:float,d:float):
    contagios_act:float=(2**d)*co
    return contagios_act
if __name__=="__main__":
    contagios_hoy:float=float(input("¿cuantos contagios hay al inicio del conteo?"))
    dias:float=float(input("¿cuantos dias se hara la cuenta?"))
    resultado=contagios(contagios_hoy,dias)
    print("despues de "+ str(dias)+" dias habran "+ str(resultado)+" contagios")
```
## Explicacion
+ Definimos una funcion la cual tome los contagios y los dias que han pasado desde ese valor de contagios
+ En esta funcion potenciamos 2 al numero de dias para despues multiplicarlo por el numero de contagios
pues por cada dia que pasa se duplica el numero de contagios
+ Ya definidas las funciones introducimos valores que se puedan añadir por teclado y aplicamos las funciones
con estos valores
+ Escribimos los resultados en un print con valores entendibles

Ejercicio 7:
Este ejercico se divide en 2 partes, una para las funciones y otra para el codigo principal
-----------
## Funciones:
```python
     a:float
b:float
c:float
d:float
e:float

def media (a,b,c,d,e):
    mid:float=(a+b+c+d+e)/5
    return mid
def mediana (a,b,c,d,e):
    global conjunto
    conjunto=(a,b,c,d,e)
    global conordenado
    conordenado=sorted(conjunto)
    valorcentral=len(conordenado)//2
    return conordenado[valorcentral] 
def promedio_multiplicativo(a,b,c,d,e):
    prom:float=(a*b*c*d*e)**0.2
    return prom
def ascendente(a,b,c,d,e):
    conasc=sorted(conjunto)
    return conasc
def descendente(a,b,c,d,e):
    condesc=sorted(conjunto,reverse=True)
    return condesc
def potencia(a,b,c,d,e):
    Maximo:float=max(conjunto)
    Minimo:float=min(conjunto)
    pot:float=Maximo**Minimo
    return pot
def raiz(a,b,c,d,e):
    Minimo:float=min(conjunto)
    radicado:float= Minimo**0.333333333333333333333333333
    return radicado     
```
## Explicacion
Se definen las 7 funciones a partir de los 5 valores que deben ser numeros reales, para esto
se usan 5 valores reales, usando en cada caso diferentes aspectos de estos
+media: Se suman y se dividen entre 5 (siempre seran 5 reales), se devuelve el resultado de esta
operacion
+mediana: Se ordenan y se elige el valor del centro dividiendo su longitud entre 2, se devuelve
el valor indicado por medio del proceso hecho con anterioridad(al ser 5 no hay que complicarse mas)
+Promedio multiplicativo: Se multiplican todos los numeros y se multiplican por 1/5 a falta de raices
+ numeros ascendentes: Se usa sorted para organizar la lista de menor a mayor
+ Numeros descendentes:Tambien se usa sorted pero hacemos la variable reverse verdadera para que
invierta el orden
+ Potencia del mayor al menor: Denominamos el mayor numero usando la max en el conjunto y hacemos
lo mismo con la min para el menor numero, hecho esto solamente operamos
+ Raiz cubica del menor numero: volvemos a obtener el valor minimo con el mismo proceso realizado en
la anterior funcion, potenciandolo por 1/3

Codigo principal:
-----------
```python
     from funcionesreto6 import*

if __name__=="__main__":
    valora:float= float(input("(numero1)a:"))
    valorb:float= float(input("(numero1)b:"))
    valorc:float= float(input("(numero1)c:"))
    valord:float= float(input("(numero1)d:"))
    valore:float= float(input("(numero1)e:"))
    
    
    mediacon:float=media(valora,valorb,valorc,valord,valore)
    print("la media de los valores es" +str(mediacon))
    medianacon:float=mediana(valora,valorb,valorc,valord,valore)
    print("la mediana es "+str(medianacon))
    promedio:float=promedio_multiplicativo(valora,valorb,valorc,valord,valore)
    print("el promedio multiplicativo es "+ str(promedio))
    simbolo=ascendente(valora,valorb,valorc,valord,valore)
    print(simbolo)
    inverso=descendente(valora,valorb,valorc,valord,valore)
    print (inverso)
    numeros1=potencia(valora,valorb,valorc,valord,valore)
    print("el resultado es "+str(numeros1))
    numeros2=raiz(valora,valorb,valorc,valord,valore)
    print("el resultado es "+ str(numeros2))

```
## Explicacion:
+ Importamos las funciones hechas en un archivo aparte, estas fueron explicadas en el punto anterior
+ Definimos 5 variables introducibles por teclado, estas seran nuestros 5 numeros reales
+ Aplicamos cada funcion con las 5 variables definidas con anterioridad
+ Usamos diferentes prints para explicar los resultados de manera entendible (en el caso de los conjuntos
solo necesitan ser mostrados)
