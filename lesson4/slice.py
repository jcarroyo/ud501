import numpy as np

def test_run():
    arr = np.random.rand(5,4)
    print arr
    print arr[0,2]
    print arr[0:2, :]
    print arr[:, 3]

def indices_run():
    a = np.random.rand(5)
    indices = np.array([1, 1, 2, 3])
    print a
    print a[indices]

def lessthanmean():
    a = np.random.rand(5, 3)
    print a
    mean = a.mean()
    print mean
    print a[a < mean]

if __name__ == "__main__":
    lessthanmean()