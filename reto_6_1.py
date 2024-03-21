
#ejercicio 1
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



