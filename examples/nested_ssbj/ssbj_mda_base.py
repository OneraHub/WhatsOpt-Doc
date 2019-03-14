# -*- coding: utf-8 -*-
"""
  ssbj_mda_base.py generated by WhatsOpt. 
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 99

import numpy as np
from openmdao.api import Problem, Group
from openmdao.api import IndepVarComp

from mda.mda import Mda

from performance import Performance
from constraints import Constraints
from mda.structure import Structure
from mda.aerodynamics import Aerodynamics
from mda.propulsion import Propulsion

class SsbjMdaBase(Group):
    """ An OpenMDAO base component to encapsulate SsbjMda MDA """

    def setup(self): 
        indeps = self.add_subsystem('indeps', IndepVarComp(), promotes=['*'])

        indeps.add_output('z', [1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
        indeps.add_output('x_aer', 1.0)
        indeps.add_output('x_str', [1.0, 1.0])
        indeps.add_output('x_pro', 1.0)
        self.add_subsystem('Mda', self.create_mda(), promotes=['Theta', 'sigma', 'x_str', 'z', 'WF', 'WT', 'dpdx', 'x_aer', 'fin', 'DT', 'ESF', 'Temp', 'x_pro', 'SFC', 'L', 'D', 'WE', 'Theta', 'sigma', 'WT', 'L', 'WE', 'x_str', 'z', 'WF', 'dpdx', 'ESF', 'Theta', 'WT', 'x_aer', 'z', 'D', 'L', 'fin', 'DT', 'ESF', 'Temp', 'D', 'x_pro', 'z', 'WE', 'SFC'])
        self.add_subsystem('Performance', self.create_performance(), promotes=['SFC', 'WF', 'WT', 'fin', 'z', 'R'])
        self.add_subsystem('Constraints', self.create_constraints(), promotes=['DT', 'ESF', 'Temp', 'Theta', 'dpdx', 'sigma', 'con1_esf', 'con2_esf', 'con_dpdx', 'con_dt', 'con_sigma1', 'con_sigma2', 'con_sigma3', 'con_sigma4', 'con_sigma5', 'con_temp', 'con_theta_low', 'con_theta_up'])

    def create_mda(self):
    	return Mda()


    def create_performance(self):
    
    	return Performance()
    
    def create_constraints(self):
    
    	return Constraints()
    


# Used by Thrift server to serve disciplines
class SsbjMdaFactoryBase(object):
    @staticmethod
    def create_performance():
    	return Performance()
            
    @staticmethod
    def create_constraints():
    	return Constraints()
            
    @staticmethod
    def create_mda_structure():
    	return Structure()
            
    @staticmethod
    def create_mda_aerodynamics():
    	return Aerodynamics()
            
    @staticmethod
    def create_mda_propulsion():
    	return Propulsion()
            
