# -*- coding: utf-8 -*-
"""
  performance_base.py generated by WhatsOpt. 
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 99

import numpy as np
from openmdao.api import ExplicitComponent

class PerformanceBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate Performance discipline """

    
    def setup(self):
		
        self.add_input('SFC', val=np.ones((1,)), desc='')
        self.add_input('WF', val=np.ones((1,)), desc='')
        self.add_input('WT', val=np.ones((1,)), desc='')
        self.add_input('fin', val=np.ones((1,)), desc='')
        self.add_input('z', val=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0], desc='')
		
        self.add_output('R', val=np.ones((1,)), desc='')
	

        