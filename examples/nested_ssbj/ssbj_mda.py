# -*- coding: utf-8 -*-
"""
  ssbj_mda.py generated by WhatsOpt. 
"""
from optparse import OptionParser
from openmdao.api import Problem
from openmdao.api import NonlinearBlockGS, ScipyKrylov
from openmdao.api import view_model
from openmdao_extensions.reckless_nonlinear_block_gs import RecklessNonlinearBlockGS
from ssbj_mda_base import SsbjMdaBase, SsbjMdaFactoryBase
from mda.mda import Mda

from performance import Performance
from constraints import Constraints

class SsbjMda(SsbjMdaBase):
    """ An OpenMDAO component to encapsulate SsbjMda analysis """
    def __init__(self, scalers):
        super(SsbjMda, self).__init__()
        self.scalers = scalers

    def create_mda(self):
    	return Mda(self.scalers)

    def create_performance(self):
        return Performance(self.scalers)

    def create_constraints(self):
        return Constraints(self.scalers)


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-n", "--no-n2", action="store_false", dest='n2_view', default=True, 
                      help="display N2 openmdao viewer")
    (options, args) = parser.parse_args()

    problem = Problem()
    problem.model = SsbjMda()

    problem.setup()
    problem.final_setup()
    
    if options.n2_view:
        view_model(problem)
    