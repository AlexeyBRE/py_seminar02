# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]
def func_first():
    nums = []
    n = int(input("Введите число: "))
    for i in range(-n, n + 1):
        nums.append(i)
    print(nums)
    nums = nums[-2:] + nums[:-2]
    print(nums)


func_first()


