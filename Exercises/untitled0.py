# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 22:39:56 2015

@author: kostas
"""

from numpy import array, dot, diag, diagflat, zeros
from numpy.linalg import norm
from pprint import pprint


def jacobi(A, b, guess, info=True, err=1e-10):
    i=0
    test = dot(A,guess) - b
    D = diag(A)
    R = A - diagflat(D)
    while norm(test) > err:
        guess = (b-dot(R, guess))/D
        i+=1
        if info:
            pprint(guess)
            pprint(i)
        test = dot(A,guess) - b
    return guess


def gauss_seidel(A, b, guess, info=True, err=1e-10):
    pass

A = array([[4.0, -1.0, 1.0],[4.0, -8.0, 1.0] , [ -2.0, 1.0, 5.0]])
b = array([7.0, -21, 15])
guess = array([1.0,2.0,2.0])

sol = jacobi(A, b, guess)