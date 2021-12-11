'''
n-dimensional point descriptor
'''

from numpy import array,arctan,tan,unique,empty,all,round
from math import degrees,radians, sqrt
from file_functions import *

"""
Class that generates an encoding composed of four components for an n-dimensional point
that is given a descriptor key.

A descriptor key is an m x 2 integer array such that its unique values equals the
set {0,...,|point| - 1}, and each row contains non-identical values.

To encode, run the method "*.transform".

To save the encoding, run the method "*.save_descriptor".
There are two options:
- save all components to a file
- save each component to a file (requires 4 files)
"""
class NDimPointDescriptor:

    def __init__(self,point, descriptorKey):#, bounds = None):
        assert len(point.shape) == 1 and point.shape[0] >= 2, "invalid point shape"
        self.point = point
        self.d1 = [] # degrees
        self.d2 = [] # distances
        self.d3 = [] # direction pairs
        assert NDimPointDescriptor.check_valid_key(descriptorKey,self.point.shape[0]),"invalid descriptor key"

        self.descriptorKey = descriptorKey

    @staticmethod
    def check_valid_key(key,keySize):
        if len(unique(key)) != keySize: return False

        for k in key:
            if len(unique(k)) != 2: return False

        return True

    def lc_for_2point(self,indexPair):
        c1 = -1 if self.point[indexPair[0]] < 0 else 1
        c2 = -1 if self.point[indexPair[1]] < 0 else 1
        return (c1,c2)

    def transf_2point(self,indexPair):
        lc = self.lc_for_2point(indexPair)
        p1,p2 = self.point[indexPair[0]] * lc[0],\
                 self.point[indexPair[1]] * lc[1]

        deg = NDimPointDescriptor.degreed(p1,p2)
        dist = sqrt(p1 ** 2 + p2 ** 2)
        return deg, dist,lc

    def transform(self):
        for d in self.descriptorKey:
            deg,dist,lc = self.transf_2point(d)
            self.d1.append(deg)
            self.d2.append(dist)
            self.d3.append(lc)

    @staticmethod
    def degreed(o, a):
        return degrees(arctan(o/a))

    """
    saves descriptor to file/s
    """
    def save_descriptor(self, fs):
        assert type(fs) is list or type(fs) is str, "invalid arg. fs"
        data = [self.d1,self.d2,self.d3,self.descriptorKey]
        if type(fs) is list:
            assert len(fs) == 4, "invalid file list length"
            for (i,f) in enumerate(fs):
                pickle_obj_to_file(data[i],f)
        else:
            pickle_obj_to_file(data,fs)
        return -1

"""
Class decodes the encoding constructed by `NDimPointDescriptor`.

Can instantiate directly with components as arguments (init) OR
with a file|fileset (load_by_files).
"""
class NDimPointScriptor:

    def __init__(self, d1,d2,d3,descriptorKey):
        self.d1 = d1 # degrees
        self.d2 = d2 # distances
        self.d3 = d3 # direction pairs

        assert len(descriptorKey.shape) == 2\
            and descriptorKey.shape[1] == 2\
            and descriptorKey.shape[0] > 0, "invalid descriptor key"
        self.descriptorKey = descriptorKey

        assert len(self.d1) == len(self.descriptorKey), "invalid d1, got {} want {}".format(len(self.d1), len(unique(self.descriptorKey)))
        assert len(self.d1) == len(self.descriptorKey), "invalid d1, got {} want {}".format(len(self.d1), len(unique(self.descriptorKey)))
        assert len(self.d3) == len(self.d1), "invalid d3"
        self.point = empty((len(unique(self.descriptorKey)),))
        return

    @staticmethod
    def load_by_files(fs):
        assert type(fs) is list or type(fs) is str, "invalid arg. fs"

        if type(fs) is list:
            assert len(fs) == 4, "invalid file list length"
            d1 = pickle_obj_from_file(fs[0])
            d2 = pickle_obj_from_file(fs[1])
            d3 = pickle_obj_from_file(fs[2])
            dk = pickle_obj_from_file(fs[3])
            return NDimPointScriptor(d1,d2,d3,dk)

        s = pickle_obj_from_file(fs)
        return NDimPointScriptor(s[0],s[1],s[2],s[3])

    def output_one(self,i):
        tv = tan(radians(self.d1[i]))
        coeff = self.solve_coeff(i,tv)
        o = coeff * tv
        a = coeff
        return (o * self.d3[i][0],a * self.d3[i][1])

    def solve_coeff(self, i, tv):
        return sqrt((self.d2[i] ** 2) / (tv ** 2 + 1))

    def transform(self):
        for i in range(self.descriptorKey.shape[0]):
            o,a = self.output_one(i)
            i1,i2 = self.descriptorKey[i,0],self.descriptorKey[i,1]
            self.point[i1],self.point[i2] = o,a
