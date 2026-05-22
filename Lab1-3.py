str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")

if len(str1) != len(str2):
    print("Ошибка: строки должны быть одинаковой длины")
elif len(str1) > 1000:
    print("Ошибка: длина строк превышает 1000 символов")
else:
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    print(distance)