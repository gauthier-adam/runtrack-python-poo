class operation:
    def __init__ (exemple, nombre1=0, nombre2=0):
        exemple.nombre1 = nombre1
        exemple.nombre2 = nombre2


 
    def addition (exemple):
        resultat = exemple.nombre1 + exemple.nombre2
        print ("le resultat est ", resultat)

operation = operation(100, 200)

operation.addition()