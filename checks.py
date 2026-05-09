import numpy as np

DELTA = 0.75


def gram_schmidt(a_vec):
    n = len(a_vec)

    a_vec = [np.array(a, dtype=np.float64) for a in a_vec]

    b_vec = []
    mu = np.zeros((n, n))

    for i in range(n):
        v = a_vec[i].copy()

        for j in range(i):
            mu[i][j] = np.dot(a_vec[i], b_vec[j]) / np.dot(b_vec[j], b_vec[j])
            v -= mu[i][j] * b_vec[j]

        b_vec.append(v)

    return b_vec, mu


def check_size_reduction(mu):
    return not any(abs(mu[i][j]) > 0.5 for i in range(len(mu)) for j in range(i))


def check_lovasz(B_star, mu, delta=DELTA):
    n = len(B_star)

    for k in range(1, n):
        left = delta * np.dot(B_star[k - 1], B_star[k - 1])

        right = np.dot(B_star[k], B_star[k]) \
            + mu[k][k - 1] ** 2 * np.dot(B_star[k - 1], B_star[k - 1])

        if left > right:
            return False

    return True


def is_lll_reduced(B, delta=DELTA, verbose=False):
    B_star, mu = gram_schmidt(B)

    size_ok = check_size_reduction(mu)
    lovasz_ok = check_lovasz(B_star, mu, delta)

    if verbose:
        print("Размер редукции:", size_ok)
        print("Условие Ловаса:", lovasz_ok)

    return size_ok and lovasz_ok