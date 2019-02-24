# -*- coding: utf-8 -*-
"""
  mod_branin_proxy.py generated by WhatsOpt. 
"""
from .mod_branin import ModBranin
from .mod_branin_conversions import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from mod_branin_base import ModBraninBase
from mod_branin_function_base import ModBraninFunctionBase


class ModBraninFunctionProxy(ModBraninFunctionBase):
    def __init__(self, proxy):
        super(ModBraninFunctionProxy, self).__init__()
        self._proxy = proxy
        
    def compute(self, inputs, outputs):
        output = self._proxy.compute_mod_branin_function(to_thrift_mod_branin_function_input(inputs))
        to_openmdao_mod_branin_function_outputs(output, outputs)



class ModBraninProxy(ModBraninBase):
    
    def __init__(self):
        super(ModBraninProxy, self).__init__()
        transport = TSocket.TSocket('localhost', 31400)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        self._proxy = ModBranin.Client(protocol)
        transport.open()

    
    def create_mod_branin_function(self):
        return ModBraninFunctionProxy(self._proxy)
    

    def ping(self):
        self._proxy.ping()

    def shutdown(self):
        self._proxy.shutdown()
    