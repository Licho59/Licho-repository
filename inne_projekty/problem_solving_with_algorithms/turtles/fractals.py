import numpy as np

def kochenize(a, b):
    HFACTOR = (3**0.5) / 6
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    mid = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
    p1 = (a[0] + dx / 3, a[1] + dy / 3)
    p3 = (b[0] - dx / 3, b[1] - dy / 3)
    p2 = (mid[0] - dy * HFACTOR, mid[1] + dx * HFACTOR)
    return p1, p2, p3


def koch(steps, width=1):
    arraysize = 4**steps + 1
    points = [(0.0, 0.0)] * arraysize
    points[0] = (-width / 2., 0.0)
    points[-1] = (width / 2., 0.0)
    stepwidth = arraysize - 1
    for n in xrange(steps):
        segment = (arraysize - 1) / stepwidth
        for s in xrange(segment):
            st = s * stepwidth
            a = (points[st][0], points[st][1])
            b = (points[st + stepwidth][0], points[st + stepwidth][1])
            index1 = st + (stepwidth) / 4
            index2 = st + (stepwidth) / 2
            index3 = st + ((stepwidth) / 4) * 3
            result = kochenize(a, b)
            points[index1], points[index2], points[index3] = result
        stepwidth /= 4
    return np.array(points)


def hilbert(n=6):
    L = []
    M = matrix([[2, 3], [1, 4]])
    for i in range(1, n):
        M1 = M.antitranspose()
        M2 = M + 4 ^ i * ones_matrix(2 ^ i)
        M3 = M + 2 * 4 ^ i * ones_matrix(2 ^ i)
        M4 = M.transpose() + 3 * 4 ^ i * ones_matrix(2 ^ i)
        P = block_matrix([[M2, M3], [M1, M4]])
        M = P
        L.append(P)

    A = M.numpy()
    nx, ny = A.shape
    Z = np.argsort(A.flatten())
    X, Y = Z % nx, Z / ny
    X, Y = X / (2 ^ n - 1.), Y / (2 ^ n - 1.)
    xy = np.vstack([X, Y]).T
    return xy
    

line(koch(1), aspect_ratio=1) + line(koch(2), color='red') + line(koch(3), color='green')