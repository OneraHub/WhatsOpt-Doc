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
        
    def setup(self):
        super(Performance, self).setup()
        self.declare_partials('*', '*')  

    def compute(self, inputs, outputs):
        """ Performance computation """
        self.perfo.compute(inputs, outputs)
			
    def compute_partials(self, inputs, partials):
        """ Jacobian for Performance """
        self.perfo.compute_partials(inputs, partials)
