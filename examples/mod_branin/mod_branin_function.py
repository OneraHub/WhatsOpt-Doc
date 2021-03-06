# -*- coding: utf-8 -*-
"""
  mod_branin_function.py generated by WhatsOpt. 
"""
import numpy as np
from mod_branin_function_base import ModBraninFunctionBase

class ModBraninFunction(ModBraninFunctionBase):
    """ An OpenMDAO component to encapsulate ModBraninFunction discipline """
		
    def compute(self, inputs, outputs):
        """ ModBraninFunction computation """
    
        x_1 = inputs['x1']
        x_2 = inputs['x2']
        # f
        part1 = (x_2-(5.1*x_1**2)/(4.*np.pi**2)+5.*x_1/np.pi-6.)**2
        part2 = 10.*((1.-1./(8.*np.pi))*np.cos(x_1)+1.)
        part3 = (5.*x_1+25.)/15.
        outputs['f'] = part1 + part2 + part3
        
        # g
        x_g1 = (x_1-2.5)/7.5
        x_g2 = (x_2-7.5)/7.5
        part1 = (4.-2.1*x_g1**2+(x_g1**4)/3.)*x_g1**2
        part2 = x_g1*x_g2
        part3 = (4.*x_g2**2-4.)*x_g2**2
        part4 = 3.*np.sin(6.*(1.-x_g1))
        part5 = 3.*np.sin(6.*(1.-x_g2))
        outputs['g'] = -(part1+part2+part3+part4+part5-6.)
        print(outputs)
        
# Reminder: inputs of compute()
#   
#       inputs['x1'] -> shape: 1, type: Float    
#       inputs['x2'] -> shape: 1, type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup()
#        super(ModBraninFunction, self).setup()
#        declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for ModBraninFunction """
#   
#       	partials['f', 'x1'] = np.zeros((1, 1))
#       	partials['f', 'x2'] = np.zeros((1, 1))
#       	partials['g', 'x1'] = np.zeros((1, 1))
#       	partials['g', 'x2'] = np.zeros((1, 1))        
