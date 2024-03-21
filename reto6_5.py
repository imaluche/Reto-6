def interes(p:float,po:float,t:float):
    valorpor= (po)/100
    costo= p(valorpor+1)**t
    return costo
if __name__=="__main__":
    prestamo:float=float(input("valor del prestamos en pesos"))
    porcentaje:float=float(input("interes mensual representado en porcentaje"))
    tiempo:float=float(input("duracion del prestamo en meses"))
    valorprestamo=interes(prestamo,porcentaje,tiempo)
    print("el presto que se tendra que pagar despues de "+str(tiempo)+" meses es "+str(valorprestamo)+" pesos")