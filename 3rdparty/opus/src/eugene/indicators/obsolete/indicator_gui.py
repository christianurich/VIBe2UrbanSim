# Opus/UrbanSim urban simulation software.
# Copyright (C) 2005-2009 University of Washington
# See opus_core/LICENSE

# open a traits-based GUI for editing PSRC indicator requests

from opus_core.indicator_framework.traits.traits_indicator_handler \
    import TraitsIndicatorHandler

try:
    import wingdbstub
except:
    pass

handler = TraitsIndicatorHandler()
handler.open_editor(package_order = ['psrc','urbansim','opus_core'])