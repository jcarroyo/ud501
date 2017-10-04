import numpy as np
import time

def get_max_index(a):
    #https://docs.scipy.org/doc/numpy/reference/routines.sort.html
    return np.argmax(a)

def test_run():
    #ROWS, COLS
    #list to 1D array
    print np.array([2,3,4])
    #list of tuples to 2D array
    print np.array([(2,3,4),(5,6,7)])
    #empty array
    print np.empty(5)
    print np.empty((5,4,3))
    #array of ones
    print np.ones((5,4))
    #array of 0
    print np.zeros((5,4), dtype=np.int32)
    #random
    print np.random.random((5,4))
    #sample from random distribution
    print np.random.normal(size=(2,3))
    print "NORMAL DISTRIBUTION", np.random.normal(50, 10, size=(2,3))

    #shape
    a = np.ones((2,6))
    print a
    print a.shape
    print "rows", a.shape[0], "cols", a.shape[1]
    print a.size
    print a.dtype

def operations():
    np.random.seed(693)
    a = np.random.randint(0, 10, size=(5,4))
    print "Array:\n", a

    print "Sum of each column:\n", a.sum(axis=0)
    print "Sum of each row:\n", a.sum(axis=1)

    #Statistics
    print "Minimum:", a.min(axis=0)
    print "Max:", a.max(axis=1)
    print "Mean:", a.mean()

if __name__ == "__main__":
    #test_run()
    #operations()
    a = np.random.random(10) * 10
    print get_max_index(a)