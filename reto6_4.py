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