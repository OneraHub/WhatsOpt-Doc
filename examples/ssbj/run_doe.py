# -*- coding: utf-8 -*-
"""
  run_doe.py generated by WhatsOpt 1.10.4
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 2

import sys
import numpy as np
import matplotlib.pyplot as plt

from openmdao.api import Problem, SqliteRecorder, CaseReader
from openmdao_extensions.smt_doe_driver import SmtDOEDriver
from ssbj_mda import SsbjMda 

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-b", "--batch",
                  action="store_true", dest="batch", default=False,
                  help="do not plot anything")
parser.add_option("-n", "--ncases", type="int",
                  dest="n_cases", default=50,
                  help="number of samples")
parser.add_option("-p", "--parallel", 
                  action="store_true", default=False,
                  help="run doe in parallel")
(options, args) = parser.parse_args()

pb = Problem(SsbjMda())
pb.driver = SmtDOEDriver(sampling_method_name='LHS', n_cases=options.n_cases, sampling_method_options={'criterion': 'ese'})
pb.driver.options['run_parallel'] = options.parallel

case_recorder_filename = 'ssbj_mda_doe.sqlite'        
recorder = SqliteRecorder(case_recorder_filename)
pb.driver.add_recorder(recorder)
pb.model.nonlinear_solver.options['err_on_non_converge'] = True


pb.model.add_design_var('x_aer', lower=0.75, upper=1.25)
pb.model.add_design_var('x_pro', lower=0.18, upper=1.81)
pb.model.add_design_var('x_str', lower=[0.4, 0.75], upper=[1.6, 1.25])
pb.model.add_design_var('z', lower=[0.2, 0.666, 0.875, 0.45, 0.72, 0.5], upper=[1.8, 1.333, 1.125, 1.45, 1.27, 1.5])



pb.model.add_objective('R', scaler=-1.)

pb.model.add_constraint('con1_esf', upper=0.)
pb.model.add_constraint('con2_esf', upper=0.)
pb.model.add_constraint('con_dpdx', upper=0.)
pb.model.add_constraint('con_dt', upper=0.)
pb.model.add_constraint('con_sigma1', upper=0.)
pb.model.add_constraint('con_sigma2', upper=0.)
pb.model.add_constraint('con_sigma3', upper=0.)
pb.model.add_constraint('con_sigma4', upper=0.)
pb.model.add_constraint('con_sigma5', upper=0.)
pb.model.add_constraint('con_temp', upper=0.)
pb.model.add_constraint('con_theta_low', upper=0.)
pb.model.add_constraint('con_theta_up', upper=0.)



pb.setup()  
pb.run_driver()        

