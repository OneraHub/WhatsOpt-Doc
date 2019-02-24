# -*- coding: utf-8 -*-
"""
  structure_base.py generated by WhatsOpt. 
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 124

import numpy as np
from openmdao.api import ExplicitComponent

class StructureBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate Structure discipline """

    
    def setup(self):
		
        self.add_input('L', val=np.ones((1,)), desc='')
        self.add_input('WE', val=np.ones((1,)), desc='')
        self.add_input('x_str', val=np.ones((2,)), desc='')
        self.add_input('z', val=np.ones((6,)), desc='')
		
        self.add_output('Theta', val=np.ones((1,)), desc='')
        self.add_output('sigma', val=np.ones((5,)), desc='')
        self.add_output('WT', val=np.ones((1,)), desc='')
        self.add_output('WF', val=np.ones((1,)), desc='')
	

        