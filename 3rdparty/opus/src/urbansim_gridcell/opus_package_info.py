# Opus/UrbanSim urban simulation software.
# Copyright (C) 2005-2009 University of Washington
# See opus_core/LICENSE 

from opus_core.opus_package import OpusPackage

class package(OpusPackage):
    name = 'urbansim_gridcell'
    required_opus_packages = ["opus_core", "urbansim"]
