# -*- coding: utf-8 -*-
"""
  run_optimization.py generated by WhatsOpt. 
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 98

import sys
import numpy as np
# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
from openmdao.api import Problem, SqliteRecorder, CaseReader, ScipyOptimizeDriver #, pyOptSparseDriver
from sellar import Sellar 


from optparse import OptionParser
parser = OptionParser()
parser.add_option("-b", "--batch",
                  action="store_true", dest="batch", default=False,
                  help="do not plot anything")
(options, args) = parser.parse_args()

pb = Problem(Sellar())

pb.driver = ScipyOptimizeDriver()
pb.driver.options['optimizer'] = 'SLSQP'


pb.driver.options['tol'] = 1.0e-06

pb.driver.options['maxiter'] = 100

pb.driver.options['disp'] = True
#pb.driver.options['debug_print'] = ['desvars','ln_cons','nl_cons','objs', 'totals']
pb.driver.options['debug_print'] = []

case_recorder_filename = 'sellar_optimization.sqlite'
print(case_recorder_filename)        
recorder = SqliteRecorder(case_recorder_filename)
# pb.add_recorder(recorder)
pb.driver.add_recorder(recorder)
pb.model.add_recorder(recorder)

# Derivatives are compute via finite-difference method
# to be commnented out if partial derivatives are declared
pb.model.approx_totals(method='fd', step=1e-6, form='central')

pb.model.add_design_var('x', lower=0, upper=10)
pb.model.add_design_var('z', lower=0, upper=10)




pb.setup()  
pb.run_driver()      

if options.batch:
    exit(0)  

# reader = CaseReader(case_recorder_filename)
# cases = reader.list_cases('problem')
# print(cases)

# for i in range(len(cases)):
#    obj = cases[i].get_objectives()
#    print(obj)      
