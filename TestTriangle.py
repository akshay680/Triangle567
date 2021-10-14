# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInvalidTriangleA(self):
        self.assertEqual(classifyTriangle(201, 2, 3), 'InvalidInput')

    def testInvalidTriangleB(self):
        self.assertEqual(classifyTriangle(1, 202, 3), 'InvalidInput')

    def testInvalidTriangleC(self):
        self.assertEqual(classifyTriangle(2, 1, 203), 'InvalidInput')

    def testInvalidTriangleD(self):
        self.assertEqual(classifyTriangle(201, 2, 203), 'InvalidInput')

    def testInvalidTriangleE(self):
        self.assertEqual(classifyTriangle(201, 202, 3), 'InvalidInput')

    def testInvalidTriangleF(self):
        self.assertEqual(classifyTriangle(2, 201, 203), 'InvalidInput')

    def testInvalidTriangleG(self):
        self.assertEqual(classifyTriangle(0, 1, 2), 'InvalidInput')

    def testInvalidTriangleH(self):
        self.assertEqual(classifyTriangle(1, 2, 0), 'InvalidInput')

    def testInvalidTriangleI(self):
        self.assertEqual(classifyTriangle(1, 0, 2), 'InvalidInput')

    def testInvalidTriangleJ(self):
        self.assertEqual(classifyTriangle(1, 0, 0), 'InvalidInput')

    def testInvalidTriangleK(self):
        self.assertEqual(classifyTriangle(0, 0, 2), 'InvalidInput')

    def testInvalidTriangleL(self):
        self.assertEqual(classifyTriangle(0, 2, 0), 'InvalidInput')

    def testInvalidTriangleM(self):
        self.assertEqual(classifyTriangle('a', 2, 3), 'InvalidInput')

    def testInvalidTriangleN(self):
        self.assertEqual(classifyTriangle(2.3, 2, 3), 'InvalidInput')

    def testInvalidTriangleO(self):
        self.assertEqual(classifyTriangle(1, 2.2, 203), 'InvalidInput')

    def testInvalidTriangleP(self):
        self.assertEqual(classifyTriangle(201, 202, 2.03), 'InvalidInput')

    def testInvalidTriangleQ(self):
        self.assertEqual(classifyTriangle(201, 'a', 2.03), 'InvalidInput')

    def testInvalidTriangleR(self):
        self.assertEqual(classifyTriangle(201, 2.02, 'b'), 'InvalidInput')

    def testInvalidTriangleS(self):
        self.assertEqual(classifyTriangle('c', 202, 2.03), 'InvalidInput')

    def testInvalidTriangleT(self):
        self.assertEqual(classifyTriangle(2.33, 2.02, 2.03), 'InvalidInput')

    def testInvalidTriangleU(self):
        self.assertEqual(classifyTriangle(1, 'a', 'b'), 'InvalidInput')

    def testInvalidTriangleV(self):
        self.assertEqual(classifyTriangle(1, 2.02, 'c'), 'InvalidInput')

    def testNotaTriangleW(self):
        self.assertEqual(classifyTriangle(1, 1, 2), 'NotATriangle')

    def testEquilateralTriangleX(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')

    def testRightTriangleY(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testScaleneTriangleZ(self):
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene')

    def testIsoscelesTriangleZ(self):
        self.assertEqual(classifyTriangle(3, 3, 5), 'Isosceles')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

