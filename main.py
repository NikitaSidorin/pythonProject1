
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
a = float(input("Введите значение выручки"))
b = float(input("Введите значение издержок "))
c = a - b
while a - b >= 0:
print(c)
   while print(c):





