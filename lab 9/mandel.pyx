import cython


cdef extern from "stdlib.h":
    void malloc(size_t size)
    void free(void *ptr)
cdef extern from "complex.h":
    double complex cpow( double complex x, double complex y)
    double cabs( double complex z );

@cython.cdivision(True)

def mandel_cy(npy, itermaxpy=100, xminpy=-2, xmaxpy=0.5, yminpy=-1.25, ymaxpy=1.25):
    '''
    Mandelbrot fractal computation using Python.

    (n, n) are the output image dimensions
    itermax is the maximum number of iterations to do.
    xmin, xmax, ymin, ymax specify the region of the
    set to compute.

    Returns a list of lists of ints, representing the image matrix with
    n rows and n columns.
    '''
    cdef:
        int n = npy
        int itermax = itermaxpy
        double xmin = xminpy
        double xmax = xmaxpy
        double ymin = yminpy
        double ymax = ymaxpy
        int ix, iy, it 
        double x, y
        double complex c, z
	
    # create list containing n lists, each containing n zeros
    # (i.e. a matrix, represented as a list of lists)
    its = [ [0] * n for i in range(n)]
    # The data in the matrix are iterations, so 'its' is the plural of
    # IT for ITeration.

    # iterate through all matrix elements
    for ix in range(0, n):
        for iy in range(0, n):
            # compute the position (x, y) corresponding to matrix element
            x = xmin + ix * (xmax - xmin) / float(n)
            y = ymin + iy * (ymax - ymin) / float(n)
            # Need to count iterations
            it = 0
            # c is the complex number with the given
            # x, y coordinates in the complex plane, i.e. c = x + i * y
            # where i = sqrt(-1)
            c = x + y * 1j
            z = 0
            # Here is the actual Mandelbrot criterion: we update z to be
            # z <- z^2 + c until |z| <= 2. We could the number of iterations
            # required. This number of iterations is the data we need to compute
            # (and plot if desired).
            while it < itermax and cabs(z) < 2.0:
                z = cpow(z, 2) + c
                it += 1

            #print("ix={}, iy={}, x={}, y={}, c={}, z={}, abs(z)={}, it={}"
            #    .format(ix, iy, x, y, c, z, abs(z), it))

            # Store the result in the matrix
            its[ix][iy] = it

    return its

