# -*- coding: utf-8 -*-
"""
  run_server.py generated by WhatsOpt. 
"""
#!/usr/bin/env python

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from server.sellar import Sellar as SellarService
from server.sellar_conversions import *
from sellar import SellarFactory as Factory

class SellarHandler:
    server = None

    def __init__(self):
        factory = Factory()
        
        self.disc1 = factory.create_disc1()
        
        self.disc2 = factory.create_disc2()
        
        self.functions = factory.create_functions()
        

    # Admin interface
    def ping(self):
        print("Ping!")

    def shutdown(self):
        print("Shutting down Sellar server...")
        exit(0)

    # Sellar interface
    
    def compute_disc1(self, ins):
        outputs = {}
        inputs = to_openmdao_disc1_inputs(ins)
        self.disc1.compute(inputs, outputs)
        return to_thrift_disc1_output(outputs)
    
    def compute_disc2(self, ins):
        outputs = {}
        inputs = to_openmdao_disc2_inputs(ins)
        self.disc2.compute(inputs, outputs)
        return to_thrift_disc2_output(outputs)
    
    def compute_functions(self, ins):
        outputs = {}
        inputs = to_openmdao_functions_inputs(ins)
        self.functions.compute(inputs, outputs)
        return to_thrift_functions_output(outputs)
    


handler = SellarHandler()
processor = SellarService.Processor(handler)
transport = TSocket.TServerSocket('0.0.0.0', port=31400)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = handler.server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print("Starting Sellar analysis server...")
server.serve()
print("done!")
