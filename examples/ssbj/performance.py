# -*- coding: utf-8 -*-
"""
  performance.py generated by WhatsOpt. 
"""
import numpy as np
from performance_base import PerformanceBase
from ssbj_openmdao.ssbj_disciplines.performance import Performance as PerformanceDiscipline

class Performance(PerformanceBase):
    """ An OpenMDAO component to encapsulate Performance discipline """
    
    def __init__(self, scalers):
        super(Performance, self).__init__()
        # scalers values
        self.perfo = PerformanceDiscipline(scalers)
        
    def compute(self, inputs, outputs):
        """ Performance computation """
        self.perfo.compute(inputs, outputs)

    def compute_partials(self, inputs, partials):
        """ Performance computation """
        self.perfo.compute_partials(inputs, partials)    
        
# Reminder: inputs of compute()
#   
#       inputs['SFC'] -> shape: (1,), type: Float    
#       inputs['WF'] -> shape: (1,), type: Float    
#       inputs['WT'] -> shape: (1,), type: Float    
#       inputs['fin'] -> shape: (1,), type: Float    
#       inputs['z'] -> shape: (6,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(Performance, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for Performance """
#   
#       	partials['R', 'SFC'] = np.zeros((1, 1))
#       	partials['R', 'WF'] = np.zeros((1, 1))
#       	partials['R', 'WT'] = np.zeros((1, 1))
#       	partials['R', 'fin'] = np.zeros((1, 1))
#       	partials['R', 'z'] = np.zeros((1, 6))        
