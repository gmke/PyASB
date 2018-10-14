#!/usr/bin/env python

'''
PyASB launcher module

Concatenate processes
____________________________

This module is part of the PyASB project, 
created and maintained by Mireia Nievas [UCM].
____________________________
'''

DEBUG = False;

__author__ = "Mireia Nievas"
__copyright__ = "Copyright 2012, PyASB project"
__credits__ = ["Mireia Nievas"]
__license__ = "GNU GPL v3"
__shortname__ = "PyASB"
__longname__ = "Python All-Sky Brightness pipeline"
__version__ = "1.99.0"
__maintainer__ = "Mireia Nievas"
__email__ = "mirph4k[at]gmail[dot]com"
__status__ = "Prototype" # "Prototype", "Development", or "Production"

try:
    import sys,os,inspect
except:
    print(str(inspect.stack()[0][2:4][::-1])+': One or more modules missing')
    raise SystemExit

class ConfigOptions():
    def __init__(self,config_file):
        self.FileOptions = []
        self.read_config_file(config_file)
    
    ''' Add and remove options '''
    def add_option(self,param,value):
        self.FileOptions.append([param,value])
    def remove_option(self,param,value):
        self.FileOptions.pop([param,value])
    
    def add_param_value(self,textline):
        line_split = textline.split("=")
        param = line_split[0].replace(' ','')
        value = line_split[1]
        if '"' not in value and "'" not in value:
            value = value.replace(' ','')
        value = value.replace('"','')
        value = value.replace("'",'')
        value = value.replace('\r','')
        value = value.replace('\n','')
        self.add_option(param,value)
        
    def read_config_file(self,config_file):
        print('Trying to open config file ...'),
        raw_config = open(config_file, 'r').readlines()
        print('OK')
        for line in xrange(len(raw_config)):
            raw_config[line] = raw_config[line].replace("\n","")
            if len(raw_config[line].split("=")) == 2:
                if raw_config[line][0]!="#":
                    self.add_param_value(raw_config[line])

