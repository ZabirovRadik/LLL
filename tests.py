from gauss import gauss_reduction
from checks import is_lll_reduced
from lll import lll_reduce

VERBOSE = True

print("ТЕСТ ГАУССОВСКОЙ РЕДУКЦИИ\n")

b1 = [105, 821]
b2 = [287, 593]

r1, r2 = gauss_reduction(b1, b2, verbose=VERBOSE)

print("Редуцированный базис (Гаусс):")
print(r1)
print(r2)

det_orig = abs(b1[0]*b2[1] - b1[1]*b2[0])
det_reduced = abs(r1[0]*r2[1] - r1[1]*r2[0])
same_lattice = (det_orig == det_reduced)

dot = r1[0]*r2[0] + r1[1]*r2[1]
len0 = r1[0]**2 + r1[1]**2
len1 = r2[0]**2 + r2[1]**2
mu = abs(dot) / len0
gauss_ok = mu <= 0.5 and len0 <= len1

is_correct = same_lattice and gauss_ok

print(f"Определитель совпадает: {'Да' if same_lattice else 'Нет'}")
print(f"Условия Гаусса: {'Да' if gauss_ok else 'Нет'}")
print(f"\nИтог: {'Корректно' if is_correct else 'Ошибка'}")

print( "\n" + "-" * 80)
print("LLL-РЕДУКЦИЯ:")

basis = [
    [2, 0, 3],
    [-30, 0, 12],
    [31, -5, 9]
]

reduced = lll_reduce(basis, verbose=VERBOSE)

print("Редуцированный базис:")
for v in reduced:
    print(v)

print("\nLLL check:")

lll_correct = is_lll_reduced(reduced, verbose=VERBOSE)
print("Корректно!" if lll_correct else "Ошибка!")

if is_correct and lll_correct:
    print("\nОба теста пройдены успешно!")