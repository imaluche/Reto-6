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