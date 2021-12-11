from file_functions import *
import unittest

class TestFileFunctions(unittest.TestCase):

    def test__create_dirpath(self):

        dp1 = "f/f1/f2"
        dp1r = "f"
        delete_dirpath(dp1r)
        create_dirpath(dp1)
        assert isdir(dp1)

        dp2 = "fx/fx1/fx2/"
        dp2r = "fx"
        delete_dirpath(dp2r)
        create_dirpath(dp2)
        assert isdir(dp2)

        # fail
        dp1f = "/w/w2"
        try:
            create_dirpath(dp1f)
            assert False, "invalid dir. path 1"
        except:
            pass

        dp2f = "w/w2.txt"
        try:
            create_dirpath(dp2f)
            assert False, "invalid dir. path 2"
        except:
            pass

    def test__pickle_obj_to_file__AND__pickle_obj_from_file(self):

        obj = [12,24,50]
        fp = "f/f1/t.txt"

        pickle_obj_to_file(obj,fp)
        assert pickle_obj_from_file(fp) == obj, "pickling failed"

        fp = "fr"
        pickle_obj_to_file(obj,fp)
        assert pickle_obj_from_file(fp) == obj, "pickling failed"


if __name__ == "__main__":
    unittest.main()
