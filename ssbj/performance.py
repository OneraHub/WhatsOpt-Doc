# -*- coding: utf-8 -*-
"""
  performance.py generated by WhatsOpt. 
"""
from performance_base import PerformanceBase
from ssbj_openmdao.disciplines.performance import Performance as PerformanceDiscipline

class Performance(PerformanceBase):
    """ An OpenMDAO component to encapsulate Performance discipline """
    def __init__(self, scalers):
        super(Performance, self).__init__()
        # scalers values
        self.perfo = PerformanceDiscipline(scalers)
        
    def compute(self, inputs, outputs):
        """ Performance computation """
        self.perfo.compute(inputs, outputs)

	
# To declare partial derivatives computation ...
# 
#    def setup()
#        super(Performance, self).setup()
#        declare_partials('*', '*')  
			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for Performance """
    
   		
#       	partials['R', 'SFC'] = np.zeros((1, 1))
#       	partials['R', 'WF'] = np.zeros((1, 1))
#       	partials['R', 'WT'] = np.zeros((1, 1))
#       	partials['R', 'fin'] = np.zeros((1, 1))
#       	partials['R', 'z'] = np.zeros((1, 6))        
