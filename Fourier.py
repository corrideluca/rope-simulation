from DepineF2 import soga
import numpy as np # ya que hay cosenos y senos lo mas probable es que usemos numpy

L = 10 #m
T = 120 #N
d = 2 #g/cm
v = (T/d)**.5 #velocidad de fase

#este es nuestro favorito

#como nos enseñaron lxs mejores profesores de F2 de la histora,
#las condiciones iniciales las vamos a dar a partir de una funcion
#por ahora solo hicimos para la de posicion inicial, la de velocidad la vamos
#a meter en github uno de estos dias :D


#definimos una funcion que sería la forma inicial de la soga
def F(x) : return(np.sin(np.pi*x/(L))+(1/3)*np.sin(3*np.pi*x/L)+(1/5)*np.sin(5*np.pi*x/L))

#este es el ejercicio 16 de la guía.

#creamos nuestro objeto

cuerda = soga.CondicionesIniciales("cerrado",L,v,F,range(100)) #le metemos F como el ultimo parametro :D
#el range(100) es el rango de modos que se va a usar para la suma, en este caso del 0 al 99


#ahora obviamente van a querer ver los graficos:

#cuerda.get_graph()

#y como hay grafico, tambien hay animación

anim = cuerda.animate(800) #le paso como parametro los frames

#si por alguna razon, no queres los graficos y queres la ecuacion mas general

#cuerda.get_ecuation(x,t) le pasas para un cierto x y t, puede ser (x,0) con x array de numpy