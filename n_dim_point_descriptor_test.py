from n_dim_point_descriptor import *
import unittest

class TestNDimPointDescriptorClass(unittest.TestCase):

    def test__descript_script_test_case_1(self):
        # description
        p = array([3,14])
        dk = array([(0,1)])
        npd = NDimPointDescriptor(p,dk)
        npd.transform()

        # scription
        nps = NDimPointScriptor(npd.d1,npd.d2,npd.d3,dk)
        nps.transform()

        assert all(nps.point == p), "incorrect description"

    def test__descript_script_test_case_2(self):

        p = array([3,14,20,-5,-31])
        dk = array([(0,1),(4,1),(2,3)])
        npd = NDimPointDescriptor(p,dk)

        npd.transform()

        nps = NDimPointScriptor(npd.d1,npd.d2,npd.d3,dk)
        nps.transform()

        assert all(round(nps.point,5) == round(p,5)), "incorrect description,\ngot {}\n want {}".format(nps.point,p)
        return

    def test__descript_script_test_case_3(self):

        p = array([310.5,-4140,0.2,15,3.1,-1501010,2412])
        dk = array([(0,6),(4,6),(2,6),(1,3),(3,5)])
        npd = NDimPointDescriptor(p,dk)

        npd.transform()

        nps = NDimPointScriptor(npd.d1,npd.d2,npd.d3,dk)
        nps.transform()

        assert all(round(nps.point,5) == round(p,5)), "incorrect description,\ngot {}\n want {}".format(nps.point,p)
        return

    def test__descript_script_test_case_4(self):

        p = array([310.5,-4140,0.2,15,3.1,-1501010,2412])
        dk = array([(0,6),(1,3),(2,4),(1,5)])
        npd = NDimPointDescriptor(p,dk)

        npd.transform()

        nps = NDimPointScriptor(npd.d1,npd.d2,npd.d3,dk)
        nps.transform()

        assert all(round(nps.point,5) == round(p,5)), "incorrect description,\ngot {}\n want {}".format(nps.point,p)
        return

    def test__descript_script_test_case_5(self):

        p = array([310.5,-4140,0.2,15,3.1,-1501010,2412])
        dk = array([(0,6),(4,6),(2,6),(1,3),(5,5)])

        try:
            npd = NDimPointDescriptor(p,dk)
            assert False, "invalid key should not work"
        except:
            pass

    def test__descript_script_test_case_6(self):

        p = array([0.3105,-0.04140,0.002,1.0005,0.3001,-0.1501010,2.412])
        dk = array([(0,6),(4,6),(2,6),(1,3),(3,5)])
        npd = NDimPointDescriptor(p,dk)

        npd.transform()

        nps = NDimPointScriptor(npd.d1,npd.d2,npd.d3,dk)
        nps.transform()

        assert all(round(nps.point,5) == round(p,5)), "incorrect description,\ngot {}\n want {}".format(nps.point,p)
        return

if __name__ == "__main__":
    unittest.main()
