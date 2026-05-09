import numpy as np
from lll import lll_reduce


def attack_congruential_lll(a, m, b):
    t = int(np.sqrt(m))
    
    basis = [
        [m, 0, 0],
        [a, 1, 0],
        [b, 0, t]
    ]
    
    reduced = lll_reduce(basis)
    
    for vec in reduced:
        if abs(int(vec[2])) == t:
            x = abs(int(vec[1]))
            if (a * x) % m == b:
                return x, reduced, basis
    return None, None, None


if __name__ == "__main__":
    a = 8731
    m = 65537
    sqrtm = int(m**0.5)
    
    tests = [5, 13, 29, 60, 100, 150, 200, 240, 255, 260, 
             300, 500, 1000, 5000]
    
    print("\nLLL-АТАКА НА КОНГРУЭНТНУЮ СХЕМУ\n")
    print(f"a = {a}, m = {m}, sqrt(m) = {sqrtm}\n")
    
    print(f"{'x':>6} {'x - sqrt(m)':>12} {'Статус':>8} {'Найдено x':>10}")
    print("-" * 70)

    for x in tests:
        b = (a * x) % m
        
        x_lll, reduced, basis = attack_congruential_lll(a, m, b)
        
        status = "+" if x_lll == x else "-"
        found = x_lll if x_lll is not None else "None"
        
        print(f"{x:>6d} {x - sqrtm:>9d} {status:>8} {found:>10}")
        
        if x == tests[5]:
            last_result = (x_lll, reduced, basis)
            last_x = x
            last_b = b

    if last_result:
        x_lll, reduced, basis = last_result
        x = last_x
        b = last_b
        
        print(f"\nДЕТАЛЬНЫЙ РАЗБОР (x = {x})")
        print(f"a = {a}")
        print(f"m = {m}")
        print(f"b = (a * x) % m = {b}")
        print(f"Ожидаемое x = {x}")
        print(f"Найденное LLL x = {x_lll}")
        print(f"Успех: {'Да' if x_lll == x else 'Нет'}\n")
        
        print("Исходный базис:")
        for row in basis:
            print(f"  {row}")
        
        print("\nLLL-редуцированный базис:")
        for row in reduced:
            print(f"  {row}")