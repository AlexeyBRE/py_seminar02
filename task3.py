# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def func_str():
    count = 0
    first_text = input("Введите текст :")
    second_text = input("Введите фразу :")
    for i in first_text:
        for j in second_text:
            if i == j:
                count += 1
        print(f'{i} - {count} ')
        count = 0
func_str()