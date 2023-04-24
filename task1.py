# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел
# от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def function_fact():
    n = int(input("Введите число: "))
    nums = []
    fact = 1
    for i in range(1, n + 1):
        nums.append(fact)
        fact *= i+1
    print(nums)

function_fact()
