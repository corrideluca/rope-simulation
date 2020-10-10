import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.integrate import quad


plt.style.use('default')
plt.style.use(['dark_background'])

class Modo():
    def __init__(self,numero_de_modo,condicion_de_contorno,length,velocidad_fase):
        self.p = numero_de_modo
        self.contorno = condicion_de_contorno
        self.length = length
        self.v = velocidad_fase
        
    def __str__(self):
        return f"modo {self.p}"
       
    def  get_k(self):
        if(self.contorno == "cerrado"):
            return (self.p * np.pi)/ self.length
        elif(self.contorno == "abierto"):
            return (self.p * np.pi) / self.length
        elif(self.contorno == "mixto"):
            return ((2*self.p - 1) * np.pi) / (2*self.length)
        else:
            return("condiciones displonibles : 'cerrado','abierto','mixto'")
        
    def get_alpha(self):
        if(self.contorno == "cerrado"):
            return 0
        elif(self.contorno == "abierto"):
            return np.pi/2
        elif(self.contorno == "mixto"):
            return 0
        else:
            raise ValueError("condiciones displonibles : 'cerrado','abierto','mixto'")
        
    def get_omega(self):
        return self.get_k()*self.v
        
    def get_ecuation(self, x, t):
        return np.sin(self.get_k()*x + self.get_alpha())*np.cos(self.get_omega()*t)
    
    def get_graph(self):
        plt.title(f"$\lambda ={((2*np.pi)/self.get_k())/self.length} L$")
        x = np.linspace(0,self.length,1000)
        return plt.plot(x,np.sin(self.get_k()*x + self.get_alpha()))
    
    def get_animation_data(self, x, t_i):
        return (x,self.get_ecuation(x,t_i))
    
    def animate(self):
        fig, ax = plt.subplots()
        line,=ax.plot([],[],zorder=3)
        ax.set_ylim(-2,2)
        ax.set_xlim(0,self.length)
        ax.set_title(f"modo {self.p} para C.C: {self.contorno}")
        x = np.linspace(0,self.length,1000)
        t = np.linspace(0,10,1000)
        def animacion(i):
            line.set_data(*self.get_animation_data(x,t[i]))
            
        return animation.FuncAnimation(fig,animacion, frames=1000, interval=100)

class CombinacionDeModos():
    def __init__(self, modos, contorno, L, velocidad_fase):
        self.p = modos
        self.contorno = contorno
        self.length = L
        self.v = velocidad_fase
    
    def get_graph(self):
        array_modos = []
        x = np.linspace(0,self.length,10000)
        for i in self.p:
            array_modos.append(Modo(i, self.contorno, self.length, self.v).get_ecuation(x, 0))
        plt.plot(x,sum(array_modos))
        
    def get_animation_data(self, x, t_i):
        array_modos = []
        x = np.linspace(0,self.length,10000)
        for i in self.p:
            array_modos.append(Modo(i, self.contorno, self.length, self.v).get_ecuation(x, t_i))
        return (x,sum(array_modos))
    
    def animate(self):
        fig, ax = plt.subplots()
        line,=ax.plot([],[],zorder=3)
        ax.set_ylim(-3,3)
        ax.set_xlim(0,self.length)
        x = np.linspace(0,self.length,1000)
        t = np.linspace(0,10,1000)
        def animacion(i):
            line.set_data(*self.get_animation_data(x,t[i]))
            
        return animation.FuncAnimation(fig,animacion, frames=1000, interval=100)

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