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