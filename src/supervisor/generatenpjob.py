'''
Created on 7 nov. 2017

@author: WIN32GG
'''

from worker import Job
import numpy as np

class Generatenpjob(Job):
    
    def setup(self, data):
        self.a = 0
    
    def loop(self, data):
        self.a += 1
        
        if(self.a > 6):
            self.shouldStop = True
            return None
        return np.random.randint(0, 255, size = (1280, 1080, 3))
    
    
    def requireData(self):
        return False