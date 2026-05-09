from lll import lll_reduce
from gauss import gauss_reduction
from attack_merkle_hellman import attack_knapsack
from atttack_congruential import attack_congruential_lll


TASK = "KNAPSACK"  # GAUSS, LLL, CONGRUENTIAL, KNAPSACK


if __name__ == "__main__":

    if TASK == "GAUSS":
        b1 = [105, 821]
        b2 = [287, 593]
        r1, r2 = gauss_reduction(b1, b2, verbose=True)
        print(f"\nr1 = {list(r1)}")
        print(f"r2 = {list(r2)}")

    elif TASK == "LLL":
        basis = [[1, 1, 1], 
                 [-1, 0, 2], 
                 [3, 5, 6]]
        reduced = lll_reduce(basis, verbose=True)
        for row in reduced:
            print(row)

    elif TASK == "CONGRUENTIAL":
        a, m = 8731, 65537
        tests = [5, 13, 100, 150, 255,300]
        for x in tests:
            b = (a * x) % m
            x_lll, _, _ = attack_congruential_lll(a, m, b)
            print(f"x = {x:>6d}  {'+' if x_lll == x else '-'}  found = {x_lll}")

    elif TASK == "KNAPSACK":
        cases = [
            ([2, 3, 7, 14, 30, 57, 120, 251], 491, 41, [1, 0, 1, 1, 0, 0, 1, 0]),
            ([3, 5, 11, 21, 44, 90, 180, 300, 600], 881, 97, [1, 1, 0, 1, 0, 1, 0, 1, 0]),
        ]
        for priv, q, r, msg in cases:
            pub = [(r * w) % q for w in priv]
            ciphertext = sum(b * k for b, k in zip(msg, pub))
            rec, _, _ = attack_knapsack(pub, ciphertext)
            print(f"msg = {msg}  ->  recovered = {rec}  {'OK' if rec == msg else 'FAIL'}")