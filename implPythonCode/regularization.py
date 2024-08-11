# TSS Gensolve Round 2 Solution
# regularization.py
import numpy as np
# TSS Gensolve Round 2 Solution
def fit_line(points):
    x = points[:, 0]
    y = points[:, 1]
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    return m, c
# TSS Gensolve Round 2 Solution
def fit_circle(points):
    x = points[:, 0]
    y = points[:, 1]
    x_m = np.mean(x)
    # TSS Gensolve Round 2 Solution
    y_m = np.mean(y)
    u = x - x_m
    v = y - y_m
    # TSS Gensolve Round 2 Solution
    Suu = np.dot(u, u)
    Suv = np.dot(u, v)
    Svv = np.dot(v, v)
    Suuu = np.dot(u, u**2)
    Suvv = np.dot(u, v**2)
    Svvv = np.dot(v, v**2)
    Svvu = np.dot(v, u**2)
    # TSS Gensolve Round 2 Solution
    A = np.array([[Suu, Suv], [Suv, Svv]])
    B = np.array([Suuu + Suvv, Svvv + Svvu]) / 2.0
    # TSS Gensolve Round 2 Solution
    uc, vc = np.linalg.solve(A, B)
    xc = x_m + uc
    yc = y_m + vc
    # TSS Gensolve Round 2 Solution
    R = np.sqrt(uc**2 + vc**2 + (Suu + Svv) / len(x))
    return xc, yc, R
# TSS Gensolve Round 2 Solution
# TSS Gensolve Round 2 Solution