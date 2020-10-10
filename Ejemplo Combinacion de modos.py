from DepineF2 import CombinacionDeModos
# si lo instalan usan:
# from F2Depine import modos y usan modos.CombinacionDeModos

L = 10 #m
T = 120 #N
d = 2 #g/cm
v = (T/d)**.5 #velocidad de fase

# creamos una variable que nos almacene esta combinacion
modos = CombinacionDeModos([1,3,4,5],"cerrado",L,v)

# le pasamos una lista que puede ser tambien un range :D en el primer parametro


#para graficar en t = 0
modos.get_graph()

#para animar esta combinacion
anim = modos.animate()

 
#supongamos que queremos los modos pares, aprovechamos el range

modos_pares = CombinacionDeModos(range(2,12,2),"cerrado",L,v)
