"""
tests for correct key uploading and unloading with file
"""
from n_dim_point_descriptor import *
import unittest

class TestNDimPointDescriptorClass__Save(unittest.TestCase):

    def test__NDimPoint__key_load_and_unload(self):
        p = array([3,14,20,-5,-31])
        dk = array([(0,1),(4,1),(2,3)])

        delete_dirpath("r")

        # upload option: 1 file
        fp = "r/f1/fx2/key1.txt"
        npd = NDimPointDescriptor(p,dk)
        npd.transform()
        npd.save_descriptor(fp)

        # unload option: 1 file
        nps = NDimPointScriptor.load_by_files(fp)
        nps.transform()
        assert all(round(nps.point,5) == round(p,5)), "[1] incorrect description,\ngot {}\n want {}".format(nps.point,p)


        # upload option: file set
        delete_dirpath("rs")
        fps = ["rs/f1/d1","rs/f2/d2","rs/f3/d3","rs/f3/fk"]
        npd.save_descriptor(fps)

        # unload option: file set
        nps = NDimPointScriptor.load_by_files(fps)
        nps.transform()
        assert all(round(nps.point,5) == round(p,5)), "[2] incorrect description,\ngot {}\n want {}".format(nps.point,p)


        # fail case
        fps = ["rs/f3331/d111","rs/f112/d21"]
        try:
            npd.save_descriptor(fps)
            assert False, "[1] invalid file set"
        except:
            pass

        try:
            nps = NDimPointScriptor.load_by_files(fps)
            assert False, "[2] invalid file set"
        except:
            pass

if __name__ == "__main__":
    unittest.main()
