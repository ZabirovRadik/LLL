import numpy as np
from lll import lll_reduce


def create_basis(public_key, ciphertext):
    n = len(public_key)
    basis = []
    for i in range(n):
        row = [0] * (n + 1)
        row[i] = 1
        row[-1] = public_key[i]
        basis.append(row)
    basis.append([0] * n + [-ciphertext])
    return basis


def recover_message(reduced, public_key, ciphertext):
    for vec in reduced:
        bits = vec[:-1]
        if all(x in (-1, 0, 1) for x in bits):
            recovered = [abs(int(x)) for x in bits]
            if sum(b * k for b, k in zip(recovered, public_key)) == ciphertext:
                return recovered
    return None


if __name__ == "__main__":
    print("\nАТАКА НА СИСТЕМУ MERKLE-HELLMAN\n")
    
    test_cases = [
        {
            "name": "Пример 1",
            "private": [2, 3, 7, 14, 30, 57, 120, 251],
            "q": 491,
            "r": 41,
            "message": [1, 0, 1, 1, 0, 0, 1, 0]
        },
        {
            "name": "Пример 2",
            "private": [3, 5, 11, 21, 44, 90, 180, 300, 600],
            "q": 881,
            "r": 97,
            "message": [1, 1, 0, 1, 0, 1, 0, 1, 0]
        },
        {
            "name": "Пример 3",
            "private": [1, 4, 9, 20, 45, 100, 200, 350, 700, 2000],
            "q": 10009,
            "r": 1013,
            "message": [0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
        }
    ]
    
    print(f"{'Пример':<12} {'n':>2} {'Сообщение':<37} {'Шифротекст':>12} {'Результат':>12}")
    print("-" * 100)
    
    for i, case in enumerate(test_cases):
        private_key = case["private"]
        q = case["q"]
        r = case["r"]
        message_bits = case["message"]
        
        public_key = [(r * w) % q for w in private_key]
        ciphertext = sum(b * k for b, k in zip(message_bits, public_key))
        
        basis = create_basis(public_key, ciphertext)
        reduced = lll_reduce(basis, verbose=False)
        
        recovered = recover_message(reduced, public_key, ciphertext)
        success = recovered == message_bits
        
        msg_str = str(message_bits)
        status = "Успех" if success else "Ошибка"
        
        print(f"{case['name']:<12} {len(private_key):>2}  {msg_str:<35} {ciphertext:>12} {status:>12}")
        
        if i == len(test_cases) - 1:
            print(f"\nДЕТАЛЬНЫЙ РАЗБОР: {case['name']}")
            print(f"Приватный ключ: {private_key}")
            print(f"Публичный ключ: {public_key}")
            print(f"Сообщение:      {message_bits}")
            print(f"Шифротекст:     {ciphertext}")
            print("\nИсходный базис:")
            for row in basis:
                print(f"  {row}")
            print("\nLLL-редуцированный базис:")
            for row in reduced:
                print(f"  {row}")
            print(f"\nВосстановлено:  {recovered}")
            print(f"Успех:          {'Да' if success else 'Нет'}")