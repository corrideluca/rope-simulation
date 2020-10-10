from DepineF2 import Modo
# si lo instalan usan:
# from F2Depine import soga y usan soga.Modo

L = 10 #m
T = 120 #N
d = 2 #g/cm
v = (T/d)**.5 #velocidad de fase

modo1 = Modo(1, "cerrado", L, v)
# El Primer parametro es el numero de modo que queremos
#el segundo son las condiciones de contorno ("abierto","cerrado","mixto")
# obviamente el tercero es L
# el cuarto es la velocidad de fase

# con esto ya tenemos todo

#si queremos el grafico del modo1

modo1.get_graph()

# si queremos obtener su omega o su k

modo1.get_omega()
modo1.get_k()

#si queremos el alpha (que nadie suele querer)

modo1.get_alpha()

# si queremos su animacion

anim = modo1.animate()

# si queremos su ecuacion (con la amplitud igualada a 1)

# modo1.get_ecuation( x ,  t  ) le pasamos como parametro un x y un t puden ser de numpy
