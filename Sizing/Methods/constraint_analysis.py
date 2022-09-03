import sys 
#This block is only necessary for me to develop the repo. Once all code is done, it shall be deleted, since normal usage of these tools will be done as a package
sys.path.append('C:\\Users\\Oscar Camargo\\UACH\\AirPyUACH')
#Not sure if this is the best method. If you want to help developing, modify the imports as you like.
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import math
import numpy as np
import matplotlib.pyplot as plt
from pint import UnitRegistry
#from SUAVE.Attributes.Atmospheres.Earth import US_Standard_1976


class configuration():
    def __init__(self):
        #self.atm = US_Standard_1976()
        self.altitudes = []
        self.rho = 0
        self.vstall = 0
        self.vv = 0
        self.takeoff_distance = 0
        self.cdmin = 0
        self.ar = 0
        self.n = 0
        self.e = 0
        self.clmax = 0
        self.clto = 0
        self.prop_eff = 0
        self.values = [['',None] for i in range(11)]
        self.ureg = UnitRegistry()
        self.vc = 0
        self.g = 9.807
        self.ws = np.linspace(1,150,150)
        self.mu = 1

    def setdefaults(self):
        #Converts every input to International Units. By default, this code and SUAVE work with that system.

        self.values[0][1].ito('kilogram / meter ** 3')

        self.values[1][1].ito('meter / second')

        self.values[2][1].ito('meter / second')

        self.values[3][1].ito("meter")
        
    def constraint_variables(self,vals_input):
        
        self.rho = vals_input[0][1].magnitude
        self.vstall = vals_input[1][1].magnitude
        self.vv = vals_input[2][1].magnitude
        self.takeoff_distance = vals_input[3][1].magnitude
        self.cdmin = vals_input[4][1]
        self.ar = vals_input[5][1]
        self.n = vals_input[6][1]
        self.e = vals_input[7][1]
        self.clmax = vals_input[8][1]
        self.clto = vals_input[9][1]
        self.prop_eff = vals_input[10][1]
        self.k = 1 / (math.pi*self.e*self.ar) #Assuming an elliptical distribution, only valid for initial sizings

    def turn(self): #Constant velocity turn
        q_turn = 0.5*(self.rho)*(self.vc**2)
        a = (self.cdmin)/(self.ws)
        b = (self.n)/(q_turn)
        return q_turn*(a + (self.k)*(b**2)*(self.ws))
    
    def roc(self): #Rate of Climb
        vy = ((2/self.rho)*self.ws*np.sqrt(self.k/(3*self.cdmin)))**0.5
        q_climb = 0.5*self.rho*(vy**2)
        return (self.vv/vy + (q_climb/self.ws)*self.cdmin) + (self.ws*self.k)/(q_climb)

    def takeoff(self): #Desired Takeoff Distance
        vto = np.sqrt(self.ws*(2/(self.rho*self.clto)))
        q_takeoff = 0.5*self.rho*(vto**2)
        cdto = self.cdmin + (self.clto**2)/(math.pi*self.e*self.ar)
        return (vto**2)/(2*self.g*self.takeoff_distance) + (q_takeoff*cdto)/self.ws + self.mu*(1-(q_takeoff*self.clto)/self.ws)

    def cruise(self): #Desired cruise Airspeed
        q_cruise = 0.5*self.rho*(self.vc**2)
        return q_cruise*self.cdmin*(1/self.ws) + self.k*(1/q_cruise)*self.ws
