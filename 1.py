
# Создание нескольких переменных
str_var = "Первая переменная"
int_var = 321
float_var = 2.24
list_var = [2, 4, 'лист']

# Вывести переменные на экран
print(str_var)
print(int_var)
print(float_var)
print(list_var)

n: int = int(input("Введите число"))
temp = str(n)
t1 = temp + temp
t2 = temp + temp +temp
comp = n + int(t1) + int(t2)
print("Резульат равен:", comp)

# Ввод положительного числа и нахождения большего числа.
n = int(input("Введите число"))
max1 = n % 10
n = n // 10
while n > 0:

   if n % 10 > max1:
     max1 = n % 10
   n = n // 10
print("Максимальная цифра в числе" , max1)

# Задача на прибыль
a = int(input("Введите значение прибыли






























# задача про спорт
print("Введите x:")
x = int(input())
print("Введите y:")
y = int(input())
s = x
k = 1
while s <= y:
    k = k+1
    s = 1.1*s
print("k = ", k, end = '')






