#from 
import physics as p
from physics import *

 












class TestPhysics(unittest.TestCase):
#problem 1 test
    test_calculate_buoyancy(self):
    self.assertAlmostEqual(p.calculate_buoyancy(1,1), 9.81)    
#problem 2 test
    test_will_it_float(self):
    self.assertTrue(will_it_float(1001,1))
    self.assertFalse(will_it_float(1,1001))
    self.assertAlmostEqual(will_it_float(1,0), "volume can't be zero")
#problem 3 test
    def test_calculate_pressure(self):
        self.assertAlmostEqual(calculate_pressure(1),9810)
#problem 4 test 
    def tes_calculate_acceleration(self):
        self.assertAlmostEqual(calculate_acceleration(5,1), 5)
        self.assertAlmostEqual(calculate_acceleration(5,0), 0)



#problem 6 test 
    def test _calc_torque(self):
        self.assertAlmostEqual(physics.calc.torque(0, 1), 0)
        self.assertAlmostEqual(physics.calc.torque(10, 0, 1), 0)
        self.assertAlmostEqual(physics.calc.torque(10, math.pi / 2, 1), 10)
            physics.calc_torque(10, 10, 0)
#problem 7
    def test _calculate_mom_inertia(self):
        self.assertAlmostEqual(physics.calc_mom_inertia(0, 0, 1), 0)
        self.assertAlmostEqual(physics.calc_mom_inertia(10, 0, 1), 0)
        self.assertAlmostEqual(physics.calc_mom_inertia(10, math.pi / 2, 1), 10)

        


