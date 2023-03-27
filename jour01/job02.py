class operation:
    def __init__ (exemple, nombre1=0, nombre2=0):
        exemple.nombre1 = nombre1
        exemple.nombre2 = nombre2
operation = operation (100, 200)
print ("le nombre1 est ", operation.nombre1)
print ("le nombre2 est ", operation.nombre2)