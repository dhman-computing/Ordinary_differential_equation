from input_function import p, q


def k_1(i, x):
    return (i*(i-1)*(x**(i-2)))


def k_2(i, x):
    return (i*p(x)*(x**(i-1)))


def k_3(i, x):
    return (q(x)*(x**(i)))


def C_ij(i, x):
    return (k_1(i, x) + k_2(i, x) + k_3(i, x))
