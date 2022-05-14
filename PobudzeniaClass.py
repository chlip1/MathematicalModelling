from math import sin, pi
from numpy import sign

class Pobudzenia:   
    
    def __init__(self,time,amp,freq):

        self.h = 0.01        
        self.T = time 
        self.M = amp        
        self.f = 2 * pi * freq       
        self.sim_steps = int(self.T/self.h)    
 
    def pobudzenie_skok(self):   # pobudzenie skokiem
        u_skok = []
        for i in range(0, self.sim_steps):
            u_skok.append(1)  
        return u_skok           

    def pobudzenie_sin(self):   # pobudzenie sinusoida o czestotliwosci f i amplitudzie M
        u_sinus = []
        for i in range(0, self.sim_steps):
            u_value = self.M * sin(self.f * i * self.h)    
            u_sinus.append(u_value)
        return u_sinus 

    def pobudzenie_prostokat(self):   # pobudzenie fala prostokatna o czestotliwosci f i amplitudzie M
        u_prostokat = []
        for i in range(0, self.sim_steps):
            u_value = self.M * sign(sin(self.f * i * self.h))  
            u_prostokat.append(u_value)
        return u_prostokat 