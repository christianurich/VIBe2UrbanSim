# Opus/UrbanSim urban simulation software.
# Copyright (C) 2005-2009 University of Washington
# See opus_core/LICENSE 

import os
import sys

from optparse import OptionParser

from classes.create_job_building_types_table import CreateJobBuildingTypesTable
    
from opus_core.database_management.configurations.database_server_configuration import DatabaseServerConfiguration

    
parser = OptionParser()
    
parser.add_option("-o", "--host", dest="host", type="string",
    help="The mysql host (default: 'localhost').")
parser.add_option("-u", "--username", dest="username", type="string",
    help="The mysql connection password (default: nothing).")
parser.add_option("-p", "--password", dest="password", type="string",
    help="The mysql connection password (default: nothing).")
parser.add_option("-d", "--database", dest="database", 
    type="string", help="The database to convert. (REQUIRED)")
    
(options, args) = parser.parse_args()

if options.host == None: options.host = 'localhost'
if options.username == None: 
    options.username = ''
if options.password == None: 
    options.password = 
''
    
if options.database == None: 
        parser.print_help()
        sys.exit(1)
    
config = DatabaseServerConfiguration(
    host_name = options.host,
    protocol = 'mysql',
    user_name = options.username,
    password = options.password,
    )

CreateJobBuildingTypesTable().create_building_types_table(config, options.database)

print 'Done.'