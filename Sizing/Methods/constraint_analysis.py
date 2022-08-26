import sys 
#This block is only necessary for me to develop the repo. Once all code is done, it shall be deleted, since normal usage of these tools will be done as a package
sys.path.append('C:\\Users\\Oscar Camargo\\UACH\\AirPyUACH')
#Not sure if this is the best method. If you want to help developing, modify the imports as you like.
import math
import numpy as np
import matplotlib.pyplot as plt
from config import aircraft,conditions

class analysis(aircraft,conditions):
    super().__init__()
