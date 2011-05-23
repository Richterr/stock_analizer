"""
Unit tests for filters module.
"""

import unittest
from coverage.stream import testindicator
from market.stream.filters import *


#----------------------------------------------------------------------
Grather_Test = testindicator(__name__, "Grather_Test",
#----------------------------------------------------------------------
Grather, (
    ((-51.56,), (None,)),
    ((-12.21,), (None,)),
    ((-0.934,), (None,)),
    ((5.9234,), (5.9234,)),
    ((4.9043,), (4.9043,)),
    ((1.5543,), (1.5543,)),
    ((-7.707,), (None,)),
    ((-3.457,), (None,)),
    ((8.9776,), (8.9776,)),
    ((-7.165,), (None,)),
    ((6.1763,), (6.1763,)),
    ((0,),      (None,)),
    ((3.0776,), (3.0776,)),
    ((-24.21,), (None,)),
    ((-46.19,), (None,)),
), base=0)


#----------------------------------------------------------------------
GratherEqual_Test = testindicator(__name__, "GratherEqual_Test",
#----------------------------------------------------------------------
GratherEqual, (
    ((-51.56,), (None,)),
    ((5,),      (5,)),
    ((-0.934,), (None,)),
    ((5.9234,), (5.9234,)),
    ((4.9043,), (None,)),
    ((1.5543,), (None,)),
    ((-7.707,), (None,)),
    ((-3.457,), (None,)),
    ((8.9776,), (8.9776,)),
    ((-7.165,), (None,)),
    ((6.1763,), (6.1763,)),
    ((0,),      (None,)),
    ((3.0776,), (None,)),
    ((-24.21,), (None,)),
    ((-46.19,), (None,)),
), base=5)


#----------------------------------------------------------------------
Lesser_Test = testindicator(__name__, "Lesser_Test",
#----------------------------------------------------------------------
Lesser, (
    ((-51.56,), (-51.56,)),
    ((5,),      (None,)),
    ((-0.934,), (-0.934,)),
    ((5.9234,), (None,)),
    ((4.9043,), (4.9043,)),
    ((1.5543,), (1.5543,)),
    ((-7.707,), (-7.707,)),
    ((-3.457,), (-3.457,)),
    ((8.9776,), (None,)),
    ((-7.165,), (-7.165,)),
    ((6.1763,), (None,)),
    ((0,),      (0,)),
    ((3.0776,), (3.0776,)),
    ((-24.21,), (-24.21,)),
    ((-46.19,), (-46.19,)),
), base=5)


#----------------------------------------------------------------------
LesserEqual_Test = testindicator(__name__, "LesserEqual_Test",
#----------------------------------------------------------------------
LesserEqual, (
    ((-51.56,), (-51.56,)),
    ((-1,),     (-1,)),
    ((-0.934,), (None,)),
    ((5.9234,), (None,)),
    ((4.9043,), (None,)),
    ((1.5543,), (None,)),
    ((-7.707,), (-7.707,)),
    ((-3.457,), (-3.457,)),
    ((8.9776,), (None,)),
    ((-7.165,), (-7.165,)),
    ((6.1763,), (None,)),
    ((0,),      (None,)),
    ((3.0776,), (None,)),
    ((-24.21,), (-24.21,)),
    ((-46.19,), (-46.19,)),
), base=-1)


# TODO: Check tests coverage

if __name__ == '__main__':
    unittest.main()