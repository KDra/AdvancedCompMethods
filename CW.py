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


def get_b(n, rho=2.0):
    """Return column vector of size n^2 containing the boundary conditions."""
    b = np.zeros(n**2)
    b[(n+1)*int(n/2.0)] = rho
    return b


def embed(A, boundary=0.0):
    """Embed the array T giving the temperature at the inner nodes in
    the domain into a larger array including the boundary temperatures
    """
    N = A.shape[0] + 2
    Afull = np.zeros((N,N))
    Afull[0] = boundary
    Afull[-1] = boundary
    Afull[:, 0] = boundary
    Afull[:, -1] = boundary
    Afull[1:-1, 1:-1] = A
    return Afull


def laplace2d(get_A, get_b, solve=sp.linalg.solve, N=20, rho=2.0):
    """Solve the Laplace equation on a 2D grid, with T=0 at all
    boundaries except y=0, where T=Te, and return an 2D array of size
    NxN giving the temperature distribution throughout the domain.
    """
    n = N-2
    A = get_A(n)
    b = get_b(n, rho)
    U = solve(A, b)
    u = U.reshape((n, n))
    ufull = embed(u)
    return ufull

def plot_pcolor(Afull):
    """Plot temperature in the domain using pcolor"""
    N = Afull.shape[0]
    x = y = np.linspace(0, 1, N)
    X, Y = np.meshgrid(x,y)
    plt.pcolor(X, Y, Afull)
    plt.axis('scaled')
    plt.colorbar()
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('u(x,y) on %dx%d grid' % (N,N))


def sor(A, b, x=None, omega=1.0, err=1e-10):
    if x == None:
        x = np.ones_like(b)
    xprev = np.zeros_like(x)
    d = np.diag(A)
    D = A - np.diagflat(d)
    while np.any(np.abs(xprev - x) > err):
        xprev=x.copy()
        for i in np.arange(len(x)):
            x[i] = omega/d[i] * (b[i] - np.dot(D[i], x)) + (1.0-omega)*x[i]
    return x


def df2(A, i, j, n=50, a=0.0, b=1.0):
    h = (b-a)/float(n)
    diff = (A[i-1, j] + A[i+1, j] - 4*A[i, j] + A[i, j-1] + A[i, j+1])
    return diff

def df2_3pt(A, i, j, n=50, a=0.0, b=1.0):
    h = (b-a)/float(n)
    diff = (-A[i-2, j] - A[i+2, j] + 16*A[i-1, j] + 16*A[i+1, j] - 60*A[i, j]
            + 16*A[i, j-1] + 16*A[i, j+1] - A[i, j-2] - A[i, j+2])
    return diff/12


def get_A2(n):
    """Return matrix A for 2D Laplace equation using block diagonal
    structure, given the number of unknowns 'n' in each direction.
    """
    Bdiag = -60 * np.eye(n)
    Bupper = 16.0*np.diag([1.0] * (n - 1), 1)
    Bupper2 = -np.diag([1.0] * (n - 2), 2)
    Blower = 16.0*np.diag([1.0] * (n - 1), -1)
    Blower2 = -np.diag([1.0] * (n - 2), -2)
    B = Bdiag + Bupper + Blower + Bupper2 + Blower2
    # Creat a list [B,B,B,...,B] with n Bs
    blst = [B] * n
    # Unpack the list of diagonal blocks 'blst'
    # since block_diag expects each block to be passed as separate
    # arguments. This is the same as doing block_diag(B,B,B,...,B)
    A = sp.linalg.block_diag(*blst)
    # Upper diagonal array offset by n: we've got (n-1) I blocks
    # each containing n ones
    Dupper = 16*np.diag(np.ones(n * (n - 1)), n)
    Dupper2 = -np.diag(np.ones(n * (n - 2)), 2*n)
    # Lower diagonal array offset by -n
    Dlower = 16*np.diag(np.ones(n * (n - 1)), -n)
    Dlower2 = -np.diag(np.ones(n * (n - 2)), -2*n)
    A += Dupper + Dlower + Dupper2 + Dlower2
    return A/12

def ex1(n=20):
    u = laplace2d(get_A, get_b, N=n, rho=2.0)
    i = len(u)
    diff = df2(u, int(i/2), int(i/2), n=n)
    if abs(diff - 2.0)<1e-6:
        print("Success! The condition $/del^2 u(0.5, 0.5) = 2.0$ is satisfied")
    else:
        print("Something went wrong del_u(0.5, 0.5)!=2.0\n")
        print(diff)

def ex2(n=20):
    u = laplace2d(get_A, get_b, solve=sor, N=n, rho=2.0)
    i = len(u)
    diff = df2(u, int(i/2), int(i/2), n=n)
    if abs(diff - 2.0)<1e-6:
        print("Success! The condition $/del^2 u(0.5, 0.5) = 2.0$ is satisfied")
    else:
        print("Something went wrong del_u(0.5, 0.5) = {} instead of 2.0\n".format(diff))


def ex3(n=20):
    u = laplace2d(get_A2, get_b, N=n, rho=2.0)
    i = len(u)
    diff = df2_3pt(u, int(i/2), int(i/2), n=n)
    if abs(diff - 2.0)<1e-6:
        print("Success! The condition $/del^2 u(0.5, 0.5) = 2.0$ is satisfied")
    else:
        print("Something went wrong del_u(0.5, 0.5) = {} instead of 2.0\n".format(diff))

ex3(25)
u1=laplace2d(get_A, get_b)

u2=laplace2d(get_A2, get_b)
"""
ufull = laplace2d(get_A, get_b)
plt.figure(1)
plt.clf()
plot_pcolor(ufull)
plt.savefig('fig06-01.pdf')"""

