# -*- coding: utf-8 -*-
"""
  ssbj.py generated by WhatsOpt. 
"""

from openmdao.api import Problem
from ssbj_base import SsbjBase
from openmdao.api import view_model
from optparse import OptionParser

# Use ssbj_openmdao as a module
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "ssbj_openmdao"))
from ssbj_openmdao import ssbj_mda

from structure import Structure
from aerodynamics import Aerodynamics
from propulsion import Propulsion
from performance import Performance
from constraints import Constraints

class Ssbj(SsbjBase):
    """ An OpenMDAO base component to encapsulate Ssbj MDA """
    pass
    def __init__(self):
        super(Ssbj, self).__init__()
        self.scalers = ssbj_mda.init_ssbj_mda()

    def create_structure(self):
        return Structure(self.scalers)

    def create_aerodynamics(self):
        return Aerodynamics(self.scalers)

    def create_propulsion(self):
        return Propulsion(self.scalers)

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
    problem.model = Ssbj()

    problem.setup()
    problem.final_setup()
    
    if options.n2_view:
        view_model(problem)
    