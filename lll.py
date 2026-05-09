import numpy as np

from checks import gram_schmidt

DELTA = 0.75


def lll_reduce(B, delta=DELTA, verbose=False):
    B = [np.array(v, dtype=np.int64) for v in B]
    n = len(B)
    k = 1
    iteration = 0

    while k < n:
        iteration += 1
        if verbose:
            print(f"\nИтерация {iteration}, k={k}")

        B_star, mu = gram_schmidt(B)
        for j in range(k-1, -1, -1):
            q = round(mu[k][j])
            if q != 0:
                B[k] = B[k] - q * B[j]
                if verbose:
                    print(f"[{iteration}] размер редукции при k={k}, j={j}, q={q}")
                    print("Updated:", B[k])
                B_star, mu = gram_schmidt(B)

        B_star, mu = gram_schmidt(B)
        left = delta * np.dot(B_star[k-1], B_star[k-1])
        right = (np.dot(B_star[k], B_star[k]) + 
                 mu[k][k-1]**2 * np.dot(B_star[k-1], B_star[k-1]))

        if left <= right:
            k += 1
        else:
            B[k], B[k-1] = B[k-1].copy(), B[k].copy()
            if verbose:
                print(f"[{iteration}] происходит перестановка {k} and {k-1}")
            k = max(k-1, 1)
    return B
