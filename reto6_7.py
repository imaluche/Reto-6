
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