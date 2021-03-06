# Opus/UrbanSim urban simulation software.
# Copyright (C) 2005-2009 University of Washington
# See opus_core/LICENSE 

import os, re
from opus_emme2.models.run_macros_abstract import RunMacrosAbstract
from opus_core.store.sftp_flt_storage import redirect_sftp_url_to_local_tempdir

class RunExportMacros(RunMacrosAbstract):
    """Class to run specified Emme2 macros. run_export_macros should run before 
       opus_emme2.models.get_emme2_data_into_cache. Then in the configuration, if there is some
       desired matrix generated by a macro, the matrix_variable_map config entry will store it.
       The macro specification should also have a specification of the bank it should run in.
    """

    def run(self, year, output_file=None):
        # if output_file is a remote sftp URL, redirect it to tempdir
        output_file = redirect_sftp_url_to_local_tempdir(output_file)

        RunMacrosAbstract.run(self, 'export_macros', year, output_file)
    
if __name__ == "__main__":
    try: import wingdbstub
    except: pass
    from optparse import OptionParser
    from opus_emme2.models.run_macros_abstract import prepare_for_running_macro
    parser = OptionParser()
    resources, options = prepare_for_running_macro(parser)
    RunExportMacros(resources).run(options.year, options.output_file)    
