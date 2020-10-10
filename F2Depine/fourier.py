import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.integrate import quad


plt.style.use('default')
plt.style.use(['dark_background'])

class CondicionesIniciales():
    def __init__(self, contorno, L, v, initial_position, rango_modos):
        self.f = initial_position
        self.modos = rango_modos
        self.length = L
        self.contorno = contorno
        self.v = v
        
        
    def fourierProcess(self, x, k):
        return self.f(x)*np.sin(k*x)
    
    def get_ecuation(self, x ,t):
        general_solution = []
        for i in self.modos:
            modo = Modo(i,self.contorno,self.length,self.v)
            Aq = (2/self.length)*quad(self.fourierProcess, 0, self.length,args=(modo.get_k()))[0]
            general_solution.append(Aq*modo.get_ecuation(x, t))
        return sum(general_solution)
        
    def get_graph(self):
        x = np.linspace(0, self.length, 1000)
        plt.plot(x, self.get_ecuation(x,0))
       
    def animate(self, frames):
        fig, ax = plt.subplots()
        line,=ax.plot([],[],zorder=3)
        x = np.linspace(0,self.length,1000)
        ax.set_ylim(-max(self.get_ecuation(x, 0)),max(self.get_ecuation(x, 0)))
        ax.set_xlim(0,self.length)
        t = np.linspace(0,10, frames)
        def animacion(i):
            line.set_data(x,self.get_ecuation(x,t[i]))
            
        return animation.FuncAnimation(fig,animacion, frames=frames, interval=100)