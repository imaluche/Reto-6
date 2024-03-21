def contagios(co:float,d:float):
    contagios_act:float=(2**d)*co
    return contagios_act
if __name__=="__main__":
    contagios_hoy:float=float(input("¿cuantos contagios hay al inicio del conteo?"))
    dias:float=float(input("¿cuantos dias se hara la cuenta?"))
    resultado=contagios(contagios_hoy,dias)
    print("despues de "+ str(dias)+" dias habran "+ str(resultado)+" contagios")