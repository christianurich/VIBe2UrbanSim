# Opus/UrbanSim urban simulation software.
# Copyright (C) 2005-2009 University of Washington
# See opus_core/LICENSE 

from urbansim.models.distribute_unplaced_jobs_model import DistributeUnplacedJobsModel as UrbansimDistributeUnplacedJobsModel

class DistributeUnplacedJobsModel(UrbansimDistributeUnplacedJobsModel):
    """
    This model works exactly as its parent. It uses different variable_package.
    It is used for locating scalable jobs into buildings.  
    """
    variable_package = "urbansim_parcel"
