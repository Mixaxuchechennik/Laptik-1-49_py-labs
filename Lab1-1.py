n = int(input("n: "))
k = int(input("k: "))

if not (1 <= n <= 40) or not (1 <= k <= 5):
    print("Ошибка: n должно быть от 1 до 40, k от 1 до 5")
else:
    if n == 1 or n == 2:
        print(1)
    else:
        m2 = 1
        m1 = 1
        for i in range(3, n + 1):
            c = m1 + k * m2
            m2, m1 = m1, c
        print(m1)
