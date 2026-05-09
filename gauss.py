import numpy as np


def gauss_reduction(b1, b2, verbose=False):
    b1 = np.array(b1, dtype=np.int64)
    b2 = np.array(b2, dtype=np.int64)

    iteration = 0

    while True:
        iteration += 1

        if np.dot(b2, b2) < np.dot(b1, b1):
            b1, b2 = b2, b1

            if verbose:
                print(f"[{iteration}] swap")
                print("b1 =", b1)
                print("b2 =", b2)

        mu = round(np.dot(b1, b2) / np.dot(b1, b1))

        if mu == 0:
            break

        b2 = b2 - mu * b1

        if verbose:
            print(f"[{iteration}] reduction")
            print("mu =", mu)
            print("b1 =", b1)
            print("b2 =", b2)

    return b1, b2