# -*- coding: utf-8 -*-
"""
  run_screening.py generated by WhatsOpt. 
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 2

import sys
import numpy as np
# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
from openmdao.api import Problem, SqliteRecorder, CaseReader
from openmdao_extensions.salib_doe_driver import SalibDOEDriver
from SALib.analyze import morris as ma
from SALib.plotting import morris as mp
from ssbj_mda import SsbjMda 
from ssbj_openmdao.ssbj_mda import get_initial_state
from ssbj_openmdao.ssbj_disciplines.common import PolynomialFunction

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-b", "--batch",
                  action="store_true", dest="batch", default=False,
                  help="do not plot anything")
(options, args) = parser.parse_args()

scalers, pf_init = get_initial_state()
# have to init pf here as pf is reimported 
# and init value computed in init_ssjb_mda is lost  
pf = PolynomialFunction(pf_init) 
pb = Problem()
pb.model = SsbjMda(scalers)
pb.driver = SalibDOEDriver(sa_method_name='Morris', sa_doe_options={'n_trajs': 10, 'n_levels': 4})
case_recorder_filename = 'ssbj_mda_screening.sqlite'        
recorder = SqliteRecorder(case_recorder_filename)
pb.driver.add_recorder(recorder)
pb.model.add_recorder(recorder)
pb.model.nonlinear_solver.add_recorder(recorder)

pb.model.add_design_var('z', lower=[0.2, 0.666, 0.875, 0.45, 0.72, 0.5], upper=[1.8, 1.333, 1.125, 1.45, 1.27, 1.5])
pb.model.add_design_var('x_aer', lower=0.75, upper=1.25)
pb.model.add_design_var('x_str', lower=[0.4, 0.75], upper=[1.6, 1.25])
pb.model.add_design_var('x_pro', lower=0.18, upper=1.81)
pb.model.add_objective('R')
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

