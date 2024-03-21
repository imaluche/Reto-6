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
