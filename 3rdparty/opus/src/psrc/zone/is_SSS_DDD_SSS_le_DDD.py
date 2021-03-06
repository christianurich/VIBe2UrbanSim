# Opus/UrbanSim urban simulation software.
# Copyright (C) 2005-2009 University of Washington
# See opus_core/LICENSE 

from opus_core.variables.variable import Variable
from variable_functions import my_attribute_label

class is_SSS_DDD_SSS_le_DDD(Variable):
    """total number of jobs for zones within DDD minutes travel time,
    The travel time used is for the home-based-work am trips by auto with 
    drive-alone.
    """
    def __init__(self, var_part1, var_part2, var_part3, number):
        self.variable = "%s_%s_%s" % (var_part1,var_part2,var_part3)
        self.number = number
        Variable.__init__(self)

    def dependencies(self):
        return [my_attribute_label(self.variable)]
    
    def compute(self, dataset_pool):
        ds = self.get_dataset()
        
        return ds.get_attribute(self.variable) <= self.number


from numpy import array
from numpy import ma

from opus_core.tests import opus_unittest
from opus_core.datasets.dataset_pool import DatasetPool
from opus_core.storage_factory import StorageFactory


class Tests(opus_unittest.OpusTestCase):
    def get_values(self, min, number):
        self.variable_name = "psrc.zone.is_employment_within_%s_minutes_travel_time_hbw_am_transit_walk_le_%s" % (min, number)
        storage = StorageFactory().get_storage('dict_storage')        
        
        storage.write_table(
            table_name='zones',
            table_data={
                "zone_id":array([1,3]),
                "number_of_jobs":array([10, 1]),
            }
        )
        storage.write_table(
            table_name='travel_data',
            table_data={
                "from_zone_id": array([3,3,1,1]),
                "to_zone_id": array([1,3,1,3]),
                "am_total_transit_time_walk": array([1.1, 2.2, 3.3, 4.4]),
            }
        )
        
        dataset_pool = DatasetPool(package_order=['urbansim'],
                                   storage=storage)

        zone = dataset_pool.get_dataset('zone')
        zone.compute_variables(self.variable_name, 
                               dataset_pool=dataset_pool)
        values = zone.get_attribute(self.variable_name)
        return values

    def test_to_2_le_9(self):
        values = self.get_values(2, 9)
        should_be = array([1, 0])
        self.assert_(ma.allequal(values, should_be), 
                     msg="Error in " + self.variable_name)

    def test_to_4_le_11(self):
        values = self.get_values(4,11)
        should_be = array([1, 1])
        self.assert_(ma.allequal(values, should_be), 
                     msg="Error in " + self.variable_name)


if __name__=='__main__':
    opus_unittest.main()