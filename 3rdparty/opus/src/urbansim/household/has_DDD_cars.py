# Opus/UrbanSim urban simulation software.
# Copyright (C) 2005-2009 University of Washington
# See opus_core/LICENSE 

from opus_core.variables.variable import Variable
from variable_functions import my_attribute_label

class has_DDD_cars(Variable):
    """has DDD cars in the household? """
    cars = "cars"
    
    def __init__(self, number):
        Variable.__init__(self)
        self.tnumber = number
        
    def dependencies(self):
        return [my_attribute_label(self.cars)]
        
    def compute(self, dataset_pool):
        return self.get_dataset().get_attribute(self.cars) == self.tnumber

    def post_check(self, values, dataset_pool):
        self.do_check("x == 0 or x==1", values)
        

from opus_core.tests import opus_unittest
from urbansim.variable_test_toolbox import VariableTestToolbox
from numpy import array
from numpy import ma
class Tests(opus_unittest.OpusTestCase):
    variable_name = "urbansim.household.has_0_cars"

    def test_my_inputs( self ):
        cars = array([0, 1, 2, 1])

        values = VariableTestToolbox().compute_variable( self.variable_name, 
            {"household":{ 
                "cars":cars}}, 
            dataset = "household" )
        should_be = array( [1,0,0,0] )
        
        self.assertEqual( ma.allclose( values, should_be, rtol=1e-7 ), True, msg = "Error in " + self.variable_name )


if __name__=='__main__':
    opus_unittest.main()