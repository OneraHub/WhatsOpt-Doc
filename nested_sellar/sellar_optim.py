# -*- coding: utf-8 -*-
"""
  sellar_optim.py generated by WhatsOpt. 
"""
from openmdao.api import Problem
from sellar_optim_base import SellarOptimBase, SellarOptimFactoryBase
from openmdao.api import view_model
from optparse import OptionParser

class SellarOptim(SellarOptimBase):
    """ An OpenMDAO base component to encapsulate SellarOptim MDA """
    pass

class SellarOptimFactory(SellarOptimFactoryBase):
    """ A factory to create disciplines of SellarOptim analysis """
    pass

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-n", "--no-n2", action="store_false", dest='n2_view', default=True, 
                      help="display N2 openmdao viewer")
    (options, args) = parser.parse_args()

    problem = Problem()
    problem.model = SellarOptim()

    problem.setup()
    problem.final_setup()
    
    if options.n2_view:
        view_model(problem)
    
