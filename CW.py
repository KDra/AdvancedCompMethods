# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 13:21:27 2015

@author: kostas
"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


def get_A(n):
    """Return matrix A for 2D Laplace equation using block diagonal
    structure, given the number of unknowns 'n' in each direction.
    """
    Bdiag = -4 * np.eye(n)
    Bupper = np.diag([1] * (n - 1), 1)
    Blower = np.diag([1] * (n - 1), -1)
    B = Bdiag + Bupper + Blower
    # Creat a list [B,B,B,...,B] with n Bs
    blst = [B] * n
    # Unpack the list of diagonal blocks 'blst'
    # since block_diag expects each block to be passed as separate
    # arguments. This is the same as doing block_diag(B,B,B,...,B)
    A = sp.linalg.block_diag(*blst)
    # Upper diagonal array offset by n: we've got (n-1) I blocks
    # each containing n ones
    Dupper = np.diag(np.ones(n * (n - 1)), n)
    # Lower diagonal array offset by -n
    Dlower = np.diag(np.ones(n * (n - 1)), -n)
    A += Dupper + Dlower
    return A


def get_b(n, x=0.5, y=0.5, rho=2.0):
    """Return column vector of size n^2 containing the boundary conditions."""
    b = np.zeros(n**2)
    b[n] = rho
    b[n+1] = rho
    return b


def embed(T, Te=100):
    """Embed the array T giving the temperature at the inner nodes in
    the domain into a larger array including the boundary temperatures
    """
    N = T.shape[0] + 2
    Tfull = np.zeros((N,N))
    Tfull[0] = Te
    Tfull[1:-1, 1:-1] = T
    return Tfull


def laplace2d(get_A, get_b, N=50, Te=100):
    """Solve the Laplace equation on a 2D grid, with T=0 at all
    boundaries except y=0, where T=Te, and return an 2D array of size
    NxN giving the temperature distribution throughout the domain.
    """
    n = N - 2
    A = get_A(n)
    b = get_b(n, Te)
    U = sp.linalg.solve(A, b)
    T = U.reshape((n, n))
    Tfull = embed(T, Te)
    return Tfull

def plot_pcolor(Tfull):
    """Plot temperature in the domain using pcolor"""
    N = Tfull.shape[0]
    x = y = np.linspace(0, 1, N)
    X, Y = np.meshgrid(x,y)
    plt.pcolor(X, Y, Tfull)
    plt.axis('scaled')
    plt.colorbar()
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('T(x,y) on %dx%d grid' % (N,N))

Tfull = laplace2d(get_A, get_b)
plt.figure(1)
plt.clf()
plot_pcolor(Tfull)
plt.savefig('fig06-01.pdf')

